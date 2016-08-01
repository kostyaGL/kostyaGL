from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import generic
from django.db.models import Count
from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Forum, Topic
from .forms import TopicForm, UserLoginForm, UserRegistrationForm


class IndexView(generic.ListView):
    template_name = 'forum/forum.html'
    context_object_name = "forum_objects_list"

    def get_queryset(self):
        return Forum.objects.annotate(Count('topic__post'))


class TopicDetailView(generic.ListView):
    template_name = 'forum/topic.html'
    context_object_name = "topic"

    def get_queryset(self):
        return Topic.objects.get(pk=self.kwargs.get('pk'))


class PostsListView(generic.ListView):
    template_name = 'forum/posts.html'
    form_class = TopicForm

    def get_queryset(self):
        return Topic.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        data = super(PostsListView, self).get_context_data(**kwargs)
        list_exam = self.get_queryset()
        number = list_exam.post_set.all()
        paginator = Paginator(number, 5)
        page = self.request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        data['posts'] = contacts
        return data

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    @method_decorator(login_required(login_url='/accounts/login/'))
    def post(self, request, **kwargs):
        post_form = TopicForm(request.POST)
        data = Topic.objects.get(pk=kwargs.get('pk'))
        if request.POST and post_form.is_valid():
            post_body = request.POST['body']
            data.post_set.create(body=post_body, creator=request.user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, 'forum/posts.html', {
                'posts': data,
                'error_message': "Body cannot be empty",
            })


class LoginView(generic.FormView):
    template_name = "forum/login.html"
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        data = super(LoginView, self).get_context_data(**kwargs)
        data['login'] = data.get('form')
        return data

    def form_valid(self, form):
        form.clean()
        user = form.login()
        if user:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return self.request.GET['next']


class RegistrationView(generic.FormView):
    template_name = 'forum/registration.html'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        data = super(RegistrationView, self).get_context_data(**kwargs)
        data['registration'] = data.get('form')
        return data

    def form_valid(self, form):
        form.clean()
        user = User.objects.create_user(form.cleaned_data.get('username'),
                                        form.cleaned_data.get('email'),
                                        form.cleaned_data.get('password'))
        user.save()
        return super(RegistrationView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return self.request.GET['next']
