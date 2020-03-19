from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type='date'

class BillingForm(forms.ModelForm):
    class Meta:
        model=Billing
        fields='__all__'
        widgets={
            'invoice_date':DateInput(),
            'delivery_date':DateInput(),
            'order_date':DateInput(),
            }

class AmountForm(forms.ModelForm):
    class Meta:
        model=Amount
        fields='__all__'
        exclude=['invoice']



