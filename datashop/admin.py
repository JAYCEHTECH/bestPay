from django.contrib import admin
from . import models


class AppPaymentAdmin(admin.ModelAdmin):
    list_display = ['username', 'payment_number', 'amount', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'payment_number', 'amount']


class AirtelTigoBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'airtime_number']


class AirtimeTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'airtime_number', 'airtime_amount', 'provider', 'reference', 'transaction_status', 'transaction_date']


class AppIShareBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'batch_id', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'bundle_number', 'batch_id']


class MTNBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'bundle_number']


class VodafoneBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'bundle_number']


class OtherMTNBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'bundle_number']


class SikaKokooBundleTransactionAdmin(admin.ModelAdmin):
    list_display = ['username', 'bundle_number', 'offer', 'reference', 'transaction_status', 'transaction_date']
    search_fields = ['reference', 'username', 'bundle_number']


class TvTransactionAdmin(admin.ModelAdmin):
    ...


class IntruderAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(models.AppPayment, AppPaymentAdmin)
admin.site.register(models.AirtelTigoBundleTransaction, AirtelTigoBundleTransactionAdmin)
admin.site.register(models.AirtimeTransaction, AirtimeTransactionAdmin)
admin.site.register(models.AppIShareBundleTransaction, AppIShareBundleTransactionAdmin)
admin.site.register(models.MTNBundleTransaction, MTNBundleTransactionAdmin)
admin.site.register(models.VodafoneBundleTransaction, VodafoneBundleTransactionAdmin)
admin.site.register(models.OtherMTNBundleTransaction, OtherMTNBundleTransactionAdmin)
admin.site.register(models.SikaKokooBundleTransaction, SikaKokooBundleTransactionAdmin)
admin.site.register(models.TvTransaction, TvTransactionAdmin)
admin.site.register(models.Intruder, IntruderAdmin)



