import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    username = ""
    login = User.objects.get(pk=1).last_login
    for u in User.objects.all():
        if(u.last_login >= login):
            login = u.last_login
            username = u.username
    user = models.CharField(max_length=150, default=username)

    def __str__(self):
        return self.question_text

    def choices(self):
        ctxt_list = []
        for choice in self.choice_set.all():
            ctxt_list.append(choice.choice_text + " con %i votos" % choice.votes)
        return ctxt_list

    def last_day_question(self):
        qlist = []
        for q in Question.objects.all():
            if q.pub_date > (timezone.now() - datetime.timedelta(days=1)):
                qlist.append(q)
        return qlist

    #Se debe importar el admin de django.contrib
    @admin.display( 
        boolean=True,
        ordering='pub_date',
        description='Published recently',
    )
    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
