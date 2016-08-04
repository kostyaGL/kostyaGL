from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Post


class UserLoginForm(ModelForm):
    class Meta:
        username = forms.CharField(min_length=5)
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

        model = User
        fields = ('username', 'password', )

    def is_user_valid(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    def clean(self):
        user = self.is_user_valid()
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self):
        user = self.is_user_valid()
        return user


class UserRegistrationForm(UserLoginForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        email = forms.EmailField()
        self.fields['email'] = email

    def clean(self):
        user = self.is_user_valid()
        if not user:
            return self.cleaned_data
        raise forms.ValidationError("This user is already exist.")


class TopicForm(ModelForm):
    class Meta:
        body = forms.CharField(widget=forms.Textarea)
        fields = ['body']
        model = Post

    def clean(self):
        user = self.is_valid()
        if not user:
            raise forms.ValidationError("Comment field cannot be empty.")
        return self.cleaned_data

