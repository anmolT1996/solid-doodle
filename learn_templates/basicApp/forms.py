from django import forms
from basicApp.models import Client

class Mform(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
