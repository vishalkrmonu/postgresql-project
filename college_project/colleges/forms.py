from django import forms
from .models import College

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name', 'college_logo', 'college_profile','instructions']
