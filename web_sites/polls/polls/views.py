from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

# from web_sites.polls import Question, Choices
# from web_sites.polls import QuestionForm, ChoicesForm
from polls.forms import QuestionForm, ChoicesForm
from polls.models import Question, Choices


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = "question_list"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['edit_list'] = Question.objects.all()
        return context

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class AddQuestionView(generic.DetailView):
    model = Question
    my_form = QuestionForm

    @staticmethod
    def post(request):
        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            choice_form = ChoicesForm(request.POST)
            if all([question_form.is_valid(), choice_form.is_valid()]):
                question = Question(
                    question_text=question_form.cleaned_data['question_text'],
                    pub_date=timezone.now())
                question.save()
                choices = request.POST.getlist('choices_text')
                for choice in choices:
                    question.choices_set.create(
                        choices_text=choice,
                        votes=0)
                return HttpResponse("saved")
            else:
                return HttpResponse('fuck')


class EditQuestionView(generic.DetailView):
    template_name = 'polls/edit_question.html'

    @staticmethod
    def post(request):
        if request.is_ajax() and request.POST:
            value = request.POST['node_to_delete']
            z = Question.objects.filter(pk=value)
            z.delete()
            return HttpResponse("delete")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




