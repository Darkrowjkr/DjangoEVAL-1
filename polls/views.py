#from django.http import Http404 # Se cambio por el get_object_or_404()
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
#from django.template import loader # Se sustituyo con render

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

    def post(self, request, *args, **kwargs):
        if(request.POST['btn']):
            question_id = request.POST['btn']
            code = Question.base64code(question_id)
            return HttpResponseRedirect(code)
        else:
            pass

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name='question'

    def get_object(self):
        question_id = Question.base64decode(self.request.path.split("/")[2])
        return Question.objects.get(id=question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name='question'

    def get_object(self):
        question_id = Question.base64decode(self.request.path.split("/")[2])
        return Question.objects.get(id=question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question':question,
            'error_message':"You didn't select a choice...",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(Question.base64code(question_id),))) #HttpResponseRedirect se usa generalmente en POST exitosos y el reverse se uso para que mandara '/polls/3/results/'