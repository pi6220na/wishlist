from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

class EditPlaceForm(forms.BaseModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited', 'visited_date', 'review_text' )