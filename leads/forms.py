import email
from socket import fromshare
from django import forms

class LeadForm(forms.Form):
    short_name = forms.CharField()
    full_name = forms.CharField()
    city = forms.CharField()
    website = forms.CharField()
    tax_number = forms.IntegerField()
    email = forms.CharField()
    status = forms.CharField()