from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # to show all the fields in the form
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags'] # to show only specific fields in the form