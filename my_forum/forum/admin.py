from django.contrib import admin

from .models import Forum, Topic, Post, MyUser


class ForumAdmin(admin.ModelAdmin):
    fields = ["title", "description", "creator", "created", "topic", "updated"]
admin.site.register([Forum, Topic, Post, MyUser])
