from django import forms
from .models import Card

class BlogForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'
    