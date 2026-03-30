from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # to show all the fields in the form
        fields = ['title', 'description','feature_image', 'demo_link', 'source_link', 'tags'] # to show only specific fields in the form
        
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), # to show tags as checkboxes instead of a dropdown
        }
        
        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            
            # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project title'})
            # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project description'})
            # self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter demo link'})
            # self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter source link'})
            # self.fields['tags'].widget.attrs.update({'class': 'input'})
            
            # or
            
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})