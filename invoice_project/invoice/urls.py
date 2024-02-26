# invoice/urls.py
from django.urls import path
from .views import create_invoice, invoice_detail

app_name = 'invoice'

urlpatterns = [
    path('', create_invoice, name='create_invoice'),
    path('detail/', invoice_detail, name='invoice_detail'),
]
