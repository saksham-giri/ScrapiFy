from .models import Scrap
from django import forms

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=[
            'seller',
            'status'
            ]
