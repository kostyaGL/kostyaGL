from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>(\d+))/$', views.TopicDetailView.as_view(), name="topic"),
    url(r'^(?P<pk>(\d+))/posts/$', views.PostsListView.as_view(), name="posts"),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/registration/$', views.RegistrationView.as_view(), name="registration"),
    url(r'^accounts/logout/$', logout, {'next_page': '/accounts/login'}),
]
