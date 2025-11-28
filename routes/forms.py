from django import forms
from .models import AirportRoute

class AirportRouteForm(forms.ModelForm):  # Form to add AirportRoute instances. for validation
    class Meta:
        model = AirportRoute
        fields = ['airport_code', 'position', 'duration']


class NthNodeSearchForm(forms.Form):   # Form to search for nth node in a direction. for validation
    direction = forms.ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right')],
        required=True
    )
    n = forms.IntegerField(min_value=1)  