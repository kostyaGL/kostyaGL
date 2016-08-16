from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from PIL import Image

from .models import Post, MyUser


class UserLoginForm(ModelForm):
    class Meta:
        username = forms.CharField(min_length=5)
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

        model = MyUser
        fields = ('username', 'password',)

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

    class Meta(UserLoginForm.Meta):
        email = forms.EmailField()
        image = forms.ImageField(widget=forms.ImageField)
        model = MyUser
        fields = UserLoginForm.Meta.fields + ('email', 'image',)

    def clean(self):
        user = self.is_user_valid()
        if not user:
            return self.cleaned_data
        raise forms.ValidationError("This user is already exist.")

    def clean_image(self):
        avatar = self.cleaned_data.get('image')
        if not avatar:
            raise forms.ValidationError("Couldn't read uploaded image")
        img = Image.open(avatar)
        sub = img.format.lower()
        if sub not in ['jpeg', 'pjpeg', 'png', 'jpg']:
            raise forms.ValidationError('Please use a JPEG or PNG image.')
        if avatar.size > (1 * 171 * 98):
            img.resize((171, 98), Image.ANTIALIAS)
            img.save(avatar.name, 'JPEG', quality=90)
        return self.cleaned_data.get('image')


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


class UserProfileForm(ModelForm):
    class Meta:
        widgets = {
            'image': forms.ClearableFileInput(),
        }
        model = MyUser
        fields = ('last_name',
                  'city',
                  'country',
                  'status',
                  'image')
    #
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
        # self.fields['image'].widget.attrs = {'id': 'selectedFile'}

