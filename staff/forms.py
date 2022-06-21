from dataclasses import fields
from email import message
from socket import fromshare
from django import forms
from staff.models import Category

class ReplyFeedbackForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = ' __all__'  
        fields = ['name'] 
