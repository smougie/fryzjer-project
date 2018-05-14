from django import forms
from .models import PriceTableWidgetPluginModel


class PriceTableWidgetForm(forms.ModelForm):
    class Meta:
        model = PriceTableWidgetPluginModel
        fields = '__all__'


