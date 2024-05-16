from typing import List

from django import forms


class CurrencyConverterForm(forms.Form):
    """
    Форма для конвертации валют. Позволяет выбрать валюты для конвертации и указать сумму.

    Атрибуты:
        from_currency (ChoiceField): Поле выбора исходной валюты.
        to_currency (ChoiceField): Поле выбора целевой валюты.
        amount (DecimalField): Поле для ввода суммы для конвертации.
    """

    def __init__(self, *args, **kwargs):
        currencies: List[str] = kwargs.pop('currencies', [])
        super().__init__(*args, **kwargs)
        self.fields['from_currency'].choices = [(currency, currency) for currency in currencies]
        self.fields['to_currency'].choices = [(currency, currency) for currency in currencies]

    from_currency = forms.ChoiceField(
        label='Из валюты',
        widget=forms.Select(attrs={'class': 'currency-select'})
    )
    to_currency = forms.ChoiceField(
        label='В валюту',
        widget=forms.Select(attrs={'class': 'currency-select'})
    )
    amount = forms.DecimalField(label='Сумма', decimal_places=2, min_value=0)
