from django import forms
from .models import ContactMeMessage


class MessageMeForm(forms.ModelForm):

    class Meta:
        model = ContactMeMessage
        fields = ("name", "email", "subject", "message")
