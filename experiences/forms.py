# experiences/forms.py
from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'technical_reflection': forms.Textarea(attrs={'rows': 4}),
            'personal_reflection': forms.Textarea(attrs={'rows': 4}),
        }
