from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import generic
from django.db.models import Count
from django.views.generic.edit import FormMixin

from .models import Forum, Topic
from .forms import TopicForm, UserLoginForm, UserRegistrationForm


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


class PostsListView(FormMixin, generic.ListView):
    template_name = 'forum/posts.html'
    form_class = TopicForm
    paginate_by = 5

    def get_queryset(self):
        return Topic.objects.prefetch_related('post_set__creator__post_set').get(
            pk=self.kwargs.get('pk')).post_set.all()

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data = self.get_queryset()
        if form.is_valid():
            form_data = Topic.objects.get(pk=self.kwargs.get('pk'))
            form_data.post_set.create(body=form.cleaned_data.get('body'), creator=self.request.user)
        self.__class__.object_list = data
        context = self.get_context_data(object_list=data)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['posts'] = context['post_list']
        context['page'] = context['page_obj']
        return context

    @method_decorator(login_required(login_url='/accounts/login/'))
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


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
