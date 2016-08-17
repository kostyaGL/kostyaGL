from django import forms
from .models import Node
from django.contrib.auth.models import User
from  django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login


class Drop_name_choice(forms.Form):
    drop_choice = (('hostname', 'hostname'), ('ip', 'ip'))
    drop_state_choice = forms.ChoiceField(choices=drop_choice)

class NodeForm(forms.ModelForm):
    class Meta:
        fields = ['hostname', 'ip']
        model = Node
        widgets = {
            'hostname': forms.TextInput(attrs={'placeholder': 'Name'}),
            'ip': forms.TextInput(attrs={'placeholder': 'Enter IPv4'}),
        }

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        }

            
