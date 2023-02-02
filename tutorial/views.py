from django.views import generic
from django.http import HttpResponseRedirect
from polls.models import Question
from django.utils import timezone
import datetime

class HomeView(generic.ListView):
    template_name = 'admin/home.html'
    context_object_name = 'last_day_question'

    def get_queryset(self):
        return Question.objects.filter(pub_date__gte=(timezone.now() - datetime.timedelta(days=1)))

    def post(self, request, *args, **kwargs):
        if(request.POST['btn']):
            question_id = request.POST['btn']
            code = Question.base64code(question_id)
            return HttpResponseRedirect('polls/' + code)
        else:
            pass