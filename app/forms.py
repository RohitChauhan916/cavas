from django.forms import ModelForm
from .models import Canvas
from django import forms

class canvasForm(forms.ModelForm):
    class Meta:
        model = Canvas
        fields = ['customer','design_image']