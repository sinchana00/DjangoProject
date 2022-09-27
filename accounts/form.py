from django import forms
from django.forms import ModelForm
from webapp.models import University

# create a form to add unis
class UniForm(ModelForm):
    class Meta:
        model = University
        fields = ('university_name', 'university_location', 'university_about',)
        labels = {
            'university_name': '',
            'university_location': '',
            'university_about': '',
        }

