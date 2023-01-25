from django.views import generic

from polls.models import Question
from django.utils import timezone
import datetime

class HomeView(generic.ListView):
    template_name = 'admin/home.html'
    context_object_name = 'last_day_question'

    def get_queryset(self):
        return Question.objects.filter(pub_date__gte=(timezone.now() - datetime.timedelta(days=1)))