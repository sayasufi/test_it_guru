from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CurrencyConverterForm
from .utils import fetch_exchange_rates
from decimal import Decimal

class ConvertCurrency(APIView):
    """
    Конечная точка API, которая обрабатывает запросы на конвертацию валют.

    Этот API принимает GET-запросы со следующими параметрами:
    - `from`: Код валюты, из которой конвертируем.
    - `to`: Код валюты, в которую конвертируем.
    - `value`: Сумма валюты для конвертации (по умолчанию 1).

    Пример запроса:
    GET /api/rates/?from=USD&to=RUB&value=1

    Пример ответа:
    {
        "result": 62.16
    }
    """

    def get(self, request) -> Response:
        """
        Обрабатывает GET-запросы на конвертацию валют на основе текущих курсов.

        Аргументы:
            request (Request): Объект HTTP-запроса, содержащий параметры `from`, `to` и `value`.

        Возвращает:
            Response: JSON-ответ, содержащий результат конвертации или сообщение об ошибке.
        """
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')
        value = Decimal(request.GET.get('value', 1))

        if not from_currency or not to_currency:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)

        exchange_data = fetch_exchange_rates()
        rates = exchange_data['rates']

        if from_currency not in rates or to_currency not in rates:
            return Response({'error': 'Currency not supported'}, status=status.HTTP_400_BAD_REQUEST)

        result = value * (rates[from_currency] / rates[to_currency])
        return Response({'result': result})


def currency_converter_view(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает запросы на конвертацию валют. Если запрос выполнен с помощью AJAX, возвращает JSON с результатом.
    В противном случае возвращает HTML-страницу с формой для конвертации валют.

    Аргументы:
        request (HttpRequest): HTTP-запрос, содержащий данные формы.

    Возвращает:
        HttpResponse: HTML-страница или JSON-ответ с результатом конвертации.
    """
    exchange_data = fetch_exchange_rates()
    rates = exchange_data['rates']
    currencies = exchange_data['currencies']

    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST, currencies=currencies)
        if form.is_valid():
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            amount = form.cleaned_data['amount']

            if from_currency in rates and to_currency in rates:
                result = amount * (rates[from_currency] / rates[to_currency])
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'result': float(result)}, status=200)
    else:
        form = CurrencyConverterForm(currencies=currencies)

    return render(request, 'converter/currency_converter.html', {'form': form})
