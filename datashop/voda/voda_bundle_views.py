from django.shortcuts import render, redirect, reverse
import requests

from .. import models
from ..forms import BundleForm
from django.contrib import messages
import json
from django.http import HttpResponse
import random
from decouple import config

def pay_for_50p_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 0.49  

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "24.05MB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_50p_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_50p_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 0.5,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVSTRDLY\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="50p Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="50p Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

########################################### 1 cedi bundle #############################################################3

def pay_for_1_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 0.99

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "65MB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_1_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_1_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 1,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDR1DLY\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="1 cedi Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="1 cedi Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

########################################### 2 cedis bundle #############################################################3

def pay_for_2_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 1.90

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "165MB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_2_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_2_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 2,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVCHTDLY\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="2 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="2 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")



# ########################################## 5 cedis bundle #############################################################3

def pay_for_5_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 4.90

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "655MB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_5_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_5_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 5.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDR5WLY\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="5 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="5 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")


########################################### 10 cedis bundle #############################################################3


def pay_for_10_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 9.90

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "1.5GB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_10_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_10_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 10.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL1\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="10 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="10 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")


########################################### 20 cedis bundle #############################################################3

def pay_for_20_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 19.50

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "4GB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_20_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_20_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 20.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL2\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="20 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="20 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")


# ########################################## 50 cedis bundle #############################################################3

def pay_for_50_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 49.50

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "10.2GB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_50_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_50_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 50.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL3\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="50 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="50 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")


########################################### 100 cedis bundle #############################################################3

def pay_for_100_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 100

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "16GB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_100_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_100_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 100.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL4\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="100 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="100 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

########################################### 200 cedis bundle #############################################################3

def pay_for_200_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 200

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
            "totalAmount": amount,
            "description": "40GB Bundle",
            "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
            "returnUrl": f'https://app.bestpaygh.com/send_200_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_200_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 200.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL5\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="200 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="200 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

########################################### 300 cedis bundle #############################################################3

def pay_for_300_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 300

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
                "totalAmount": amount,
                "description": "125GB Bundle",
                "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
                "returnUrl": f'https://app.bestpaygh.com/send_300_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_300_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 300.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL6\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="300 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="300 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

# ########################################## 400 cedis bundle #############################################################3


def pay_for_400_bundle(request):
    client_ref = 'gds'+str(random.randint(11111111, 99999999))

    if request.method == "POST":
        form = BundleForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data["phone"])
            amount = 400

            url = "https://payproxyapi.hubtel.com/items/initiate"

            payload = json.dumps({
                "totalAmount": amount,
                "description": "225GB Bundle",
                "callbackUrl": 'https://webhook.site/d53f5c53-eaba-4139-ad27-fb05b0a7be7f',
                "returnUrl": f'https://app.bestpaygh.com/send_400_voda_bundle/{client_ref}/{phone_number}',
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
            return render(request, 'store/layouts/voda_bundle.html', context={'form': form})
    else:
        form = BundleForm(initial={'phone':233})
    return render(request, "store/layouts/voda_bundle.html", {'form': form})


def send_400_bundle(request, client_ref, phone_number, username, email):
    reference = f"\"{client_ref}\""
    url = "https://cs.hubtel.com/commissionservices/2016884/fa27127ba039455da04a2ac8a1613e00"

    payload = "{\r\n    \"Destination\": " + phone_number + ",\r\n    \"Amount\": 400.0,\r\n    \"CallbackUrl\": \"https://webhook.site/9125cb31-9481-47ad-972f-d1d7765a5957\",\r\n    \"ClientReference\": " + reference + ",\r\n    \"Extradata\" : {\r\n        \"bundle\" : \"DATANVDBDL7\"\r\n    }\r\n}\r\n"
    headers = {
        'Authorization': config("HUBTEL_API_KEY"),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="400 cedis Bundle",
            reference=client_ref,
            transaction_status="Success"
        )
        new_voda_transaction.save()
        return redirect('thank_you')
    else:
        print("not 200 error")
        new_voda_transaction = models.VodafoneBundleTransaction.objects.create(
            username=username,
            email=email,
            bundle_number=phone_number,
            offer="400 cedis Bundle",
            reference=client_ref,
            transaction_status="Failed"
        )
        new_voda_transaction.save()
        return redirect("failed")

