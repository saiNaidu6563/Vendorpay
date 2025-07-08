from django.contrib import admin

from merchant_app.models import *
admin.site.register(Merchant)       # merchant_app
admin.site.register(MerchantProduct)
