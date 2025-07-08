from django.shortcuts import render
from .models import Transaction

def customer_template_view(request, transaction_id):
    txn = Transaction.objects.get(pk=transaction_id)
    return render(request, 'vendor_app/customer_view.html', {'transaction': txn})

def amazon_template_view(request, transaction_id):
    txn = Transaction.objects.get(pk=transaction_id)
    return render(request, 'vendor_app/amazon_view.html', {'transaction': txn})

def merchant_template_view(request, transaction_id):
    txn = Transaction.objects.get(pk=transaction_id)
    return render(request, 'vendor_app/merchant_view.html', {'transaction': txn})
