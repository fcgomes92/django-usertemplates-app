from django import forms
from usertemplates import models


class TemplateForm(forms.ModelForm):
    class Meta:
        model = models.Template
        fields = ['html', ]
