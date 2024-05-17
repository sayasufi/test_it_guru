# converter/urls.py

from django.urls import path
from .views import ConvertCurrency, currency_converter_view

urlpatterns = [
    path('rates/', ConvertCurrency.as_view(), name='convert_currency'),
    path('converter/', currency_converter_view, name='currency_converter_view'),
    path('', currency_converter_view, name='currency_converter_view'),
]
