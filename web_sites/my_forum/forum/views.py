from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.db.models import Count
from django.views.generic.edit import FormMixin

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


class PostsListView(FormMixin, generic.ListView):
    template_name = 'forum/posts.html'
    form_class = TopicForm
    paginate_by = 5

    def get_queryset(self):
        return (Topic.objects
                .prefetch_related('post_set__creator')
                .get(pk=self.kwargs.get('pk'))
                .post_set.all())

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['posts'] = context['post_list']
        context['page'] = context['page_obj']
        return context

    @method_decorator(login_required(login_url='/accounts/login/'))
    def post(self, request, *args, **kwargs):
        form = TopicForm(request.POST)
        if request.is_ajax() and request.POST['post_id']:
            print request.POST['post_id']

        if not form.is_valid():
            self.__class__.object_list = self.get_queryset()
            context = self.get_context_data(object_list=self.__class__.object_list)
            return self.render_to_response(context)
        else:
            form_data = Topic.objects.get(pk=self.kwargs.get('pk'))
            form_data.post_set.create(body=form.cleaned_data.get('body'),
                                      creator=self.request.user)
            self.__class__.object_list = form_data.post_set.all()
            context = self.get_context_data(object_list=self.__class__.object_list)
            return self.render_to_response(context)


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
