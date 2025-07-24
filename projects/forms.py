from django import forms
from .models import Projects

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'text': 'What would you like to add?'
        }