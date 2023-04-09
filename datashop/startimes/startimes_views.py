from django.shortcuts import render, redirect, reverse
import requests

from .. import models
from ..forms import TVForm
from django.contrib import messages
import json
from django.http import HttpResponse
import random
from decouple import config

def pay_for_startimes(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = TVForm(request.POST)
        if form.is_valid():
            account_number = str(form.cleaned_data["account_number"])
            amount = str(form.cleaned_data["amount"])

            amount_to_be_charged = amount

            float_amount = float(amount)
            if float_amount == 0.5:
                amount_to_be_charged = 0.49
            elif float_amount == 1.00:
                percentage = 0.01
                amount_to_be_charged = float_amount - percentage
            elif float_amount >= 2 and float_amount <= 10:
                percentage = 0.10
                amount_to_be_charged = float_amount - percentage
            elif float_amount >= 11 and float_amount <= 50:
                percentage = 0.50
                amount_to_be_charged = float_amount - percentage

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount_to_be_charged,
            "description": "GoTV",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_startimes_amount/{client_ref}/{account_number}/{amount}',
            "cancellationUrl": "https://www.google.com",
            "merchantAccountNumber": "2017101",
            "clientReference": client_ref
            })
            headers = {
            'Authorization': config("HUBTEL_API_KEY"),
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.json())
            data = response.json()
            print(data)

            if data["status"] == "Success":
                checkout = data['data']['checkoutUrl']
                return redirect(checkout)
            else:
                messages.info(request, "Failed. Try again later")
            return render(request, 'store/layouts/dstv.html', context={'form': form})
    else:
        form = TVForm()
    return render(request, "store/layouts/dstv.html", {'form': form})


def send_startimes_amount(request, client_ref, account_number, amount, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/6598652d34ea4112949c93c079c501ce"

    payload = "{\r\n    \"Destination\": " + account_number + ",\r\n    \"Amount\": " + amount + ",\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + "\r\n}"
    headers = {
    'Authorization': config("HUBTEL_API_KEY"),
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_airtime_transaction = models.TvTransaction.objects.create(
            username=username,
            email=email,
            account_number=account_number,
            amount=amount,
            provider="Star Times",
            reference=client_ref,
            transaction_status="Success"
        )
        new_airtime_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_airtime_transaction = models.TvTransaction.objects.create(
            username=username,
            email=email,
            account_number=account_number,
            amount=amount,
            provider="Star Times",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_airtime_transaction.save()
        return redirect("failed")


