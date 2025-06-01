from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'objective': forms.Textarea(attrs={'class': 'form-textarea'}),
            'dataset_description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'model_training': forms.Textarea(attrs={'class': 'form-textarea'}),
            'sahi_description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'results': forms.Textarea(attrs={'class': 'form-textarea'}),
            'key_learnings': forms.Textarea(attrs={'class': 'form-textarea'}),
            'technologies_used': forms.TextInput(attrs={'class': 'form-input'}),
            'project_link': forms.URLInput(attrs={'class': 'form-input'}),
            'github_link': forms.URLInput(attrs={'class': 'form-input'}),
        }
