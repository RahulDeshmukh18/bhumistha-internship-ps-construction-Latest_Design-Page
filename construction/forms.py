# contact/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'category', 'message']

    category = forms.ChoiceField(choices=[
        ('Residential', 'Residential'),
        ('Industrial', 'Industrial'),
        ('Commercial', 'Commercial'),
    ])
