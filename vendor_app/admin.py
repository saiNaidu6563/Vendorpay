from django.contrib import admin

from vendor_app.models import *
#admin.site.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.full_clean()  # Triggers .clean()
        super().save_model(request, obj, form, change)

admin.site.register(Transaction, TransactionAdmin)