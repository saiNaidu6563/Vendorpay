#  VendorPay – Django + MySQL Project

**VendorPay** is a full-stack backend project built with Django and MySQL that simulates real-world transaction flow from **Customer → Amazon → Merchant**. It manages product orders, tracks commissions, and displays data via clean **JSON APIs** and optional **HTML views**.

---

##  Tech Stack

-  Python (Django Framework)
-  MySQL Database
-  JSON APIs using `JsonResponse`
-  HTML Template Views (optional)
- MySQL Triggers for inventory control
-  Django Admin for data management

---

##  Project Modules

| Django App | Purpose |
|------------|---------|
| `amazon_app` | Manages Customers, Products, and Orders |
| `merchant_app` | Handles Merchants and their Product inventory |
| `vendor_app` | Tracks Transactions and exposes data via APIs |

---

## 🔗 Key Features

-  Tracks full money flow from Customer → Amazon (commission) → Merchant (share)
- JSON API responses for each stakeholder
- Dynamic commission + merchant share logic
-  MySQL Triggers:
  - After placing an order, reduce product stock
  - Prevent orders if stock is unavailable
-  Admin panel for data entry and testing
- Optional HTML views for browser-friendly output

---

## 🖥 JSON API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/customer/<transaction_id>/` | Shows what the customer sees (amount paid, product, address) |
| `/api/amazon/<transaction_id>/` | Shows Amazon's view (commission cut) |
| `/api/merchant/<transaction_id>/` | Shows Merchant's view (earnings) |

Example:
```json
{
  "transaction_id": 1,
  "amount_paid": "3000.00",
  "ordered": "Bluetooth Speaker",
  "address": "Mumbai, India"
}

