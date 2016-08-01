from django.contrib import admin

from .models import Question, Choices


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
admin.site.register([Question, Choices])
