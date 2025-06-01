from django import forms
from .models import AboutMe

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4}),
            'passions': forms.Textarea(attrs={'rows': 3}),
            'strengths': forms.Textarea(attrs={'rows': 3}),
        }
