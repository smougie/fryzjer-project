from django import forms
from .models import NewsListWidgetPluginModel


class NewsListWidgetForm(forms.ModelForm):
    class Meta:
        model = NewsListWidgetPluginModel
        fields = '__all__'


