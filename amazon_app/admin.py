from django.contrib import admin

from amazon_app.models import *
admin.site.register(Customer)       # amazon_app
admin.site.register(Product)
admin.site.register(Order)

