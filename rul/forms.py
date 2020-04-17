from django import forms

from .models import UserPalette, Palette


def get_user_palette_form(user_id):
    class UserPaletteForm(forms.Form):
        palettes = Palette.objects.all()
        OPTIONS = ((p.id, p.name) for p in palettes)

        initial_values = [str(p.palette.id) for p in UserPalette.objects.filter(user_id=user_id)]
        palettes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              choices=OPTIONS, initial=initial_values)

    return UserPaletteForm


class UserPaletteForm2(forms.ModelForm):
    class Meta:
        model = UserPalette
        fields = ['palette', 'user']
