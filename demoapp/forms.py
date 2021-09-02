from .models import Wishes
from django import forms
class WishForms(forms.ModelForm):
    class Meta:
        model= Wishes
        fields=['place','priority','added_date','experience']