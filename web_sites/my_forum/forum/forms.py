import StringIO
import uuid
from django import forms
from django.contrib.auth import authenticate
from django.core.files.uploadedfile import InMemoryUploadedFile
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
        if avatar.size > (1 * 271 * 158):
            img = img.resize((271, 158), Image.ANTIALIAS)
            buffer = StringIO.StringIO()
            img.save(buffer, 'JPEG', quality=90)
            image_path = InMemoryUploadedFile(buffer, None, str(uuid.uuid4()), 'image/png', buffer.len, None)
            return image_path


class TopicForm(ModelForm):
    class Meta:
        body = forms.CharField(widget=forms.Textarea)
        fields = ['body']
        model = Post

    def clean(self):
        form = self.is_valid()
        if not form:
            raise forms.ValidationError("Comment field cannot be empty.")
        return self.cleaned_data


class UserProfileForm(UserRegistrationForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

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
