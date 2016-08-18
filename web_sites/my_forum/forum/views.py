from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.db.models import Count

from .models import Forum, Topic, MyUser, Post
from .forms import TopicForm, UserLoginForm, UserRegistrationForm, UserProfileForm


class IndexView(generic.ListView):
    template_name = 'forum/forum.html'
    context_object_name = "forum_objects_list"

    def get_queryset(self):
        return (Forum.objects
                .annotate(post_number=Count('topic__post'))
                .order_by()
                .annotate(topic_number=Count("topic", distinct=True))
                .prefetch_related('creator')
                )


class TopicDetailView(generic.ListView):
    template_name = 'forum/topic.html'
    context_object_name = "topic"

    def get_queryset(self):
        try:
            return Forum.objects.prefetch_related("creator__forum_set").get(
                pk=self.kwargs.get('pk')).topic_set.all().annotate(post_number=Count('post'))
        except Topic.DoesNotExist:
            return


class PostsListView(generic.ListView):
    template_name = 'forum/posts.html'

    def get_queryset(self):
        return Topic.objects.prefetch_related('post_set__creator').get(pk=self.kwargs.get('pk'))

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

    @method_decorator(login_required(login_url='/accounts/login/'))
    def post(self, request, **kwargs):
        post_form = TopicForm(request.POST)
        data = self.get_queryset()
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
        form.instance.set_password(form.instance.password)
        form.instance.is_staff = True
        form.instance.save()
        return super(RegistrationView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return self.request.GET['next']


class UserProfileView(generic.FormView):
    template_name = 'forum/user_profile.html'
    form_class = UserProfileForm

    def get_form_kwargs(self):
        form_kwargs = super(UserProfileView, self).get_form_kwargs()
        form_kwargs.update({'instance': MyUser.objects.get(pk=self.kwargs.get('user_pk')),
                            })
        return form_kwargs

    def get_context_data(self, **kwargs):
        data = super(UserProfileView, self).get_context_data(**kwargs)
        data['profile'] = data.get('form')
        data['posts'] = Post.objects.prefetch_related("topic__forum__creator").filter(
            creator=self.kwargs.get('user_pk'))
        return data

    def form_valid(self, form):
        form.clean()
        form.save()
        return super(UserProfileView, self).form_valid(form)

    def get_success_url(self):
        return self.request.path
