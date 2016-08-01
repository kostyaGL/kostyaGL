from django import forms
from .models import Choices, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


class ChoicesForm(forms.ModelForm):
    class Meta:
        fields = ('choices_text', )
        model = Choices
