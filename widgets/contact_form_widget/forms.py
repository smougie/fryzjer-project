from django import forms
from .models import ContactFormWidgetPluginModel


class ContactFormWidgetForm(forms.ModelForm):
    class Meta:
        model = ContactFormWidgetPluginModel
        fields = '__all__'


