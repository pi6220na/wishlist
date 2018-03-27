from django import forms
from .models import Place

class DateInput(forms.DateInput):
    input_type = 'date'


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited' )

class EditPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited', 'visited_date', 'review_text' )
        widgets = {'visited_date': DateInput()}