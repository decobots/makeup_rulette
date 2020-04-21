from django import forms

from .models import PaletteRequest


class PaletteRequestForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = PaletteRequest
        exclude = ('user', 'processed', 'date')
