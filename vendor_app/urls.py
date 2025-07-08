from django.urls import path
from vendor_app import views

urlpatterns = [
    # path('customer/<int:transaction_id>/', views.transaction_customer_json),
    # path('amazon/<int:transaction_id>/', views.transaction_amazon_json),
    # path('merchant/<int:transaction_id>/', views.transaction_merchant_json),
# HTML Template Views
    path('customer/<int:transaction_id>/', views.customer_template_view),
    path('amazon/<int:transaction_id>/', views.amazon_template_view),
    path('merchant/<int:transaction_id>/', views.merchant_template_view),
]