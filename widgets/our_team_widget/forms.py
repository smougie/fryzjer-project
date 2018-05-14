from django import forms
from .models import OurTeamWidgetPluginModel


class OurTeamWidgetForm(forms.ModelForm):
    class Meta:
        model = OurTeamWidgetPluginModel
        fields = '__all__'


