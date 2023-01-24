from django.core.management.base import BaseCommand
from polls.models import Question

class Command(BaseCommand):
    help = 'Muestra los valores anterior al id mencionado'

    def add_arguments(self, parser):
        parser.add_argument('question_id', type=int, help='Indica el id del item a buscar')

    def handle(self, *args, **kwargs):
        question_id = kwargs['question_id']
        question = Question.objects.get(id=question_id)
        choices = question.choices()
        if(choices):
            self.stdout.write("Los elementos en la pregunta %i son" % question_id)
            for c in choices:
                self.stdout.write(c+"\n")
        else:
            self.stdout.write("No hay elementos en la pregunta %i" % question_id)