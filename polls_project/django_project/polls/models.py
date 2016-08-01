import datetime

from django.utils import timezone
from django.db import models


class Question(models.Model):
    class Meta:
        app_label = 'polls'
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return '%s' % self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choices_text
