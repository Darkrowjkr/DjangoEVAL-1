from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields =  ['pub_date', 'question_text', 'user] #Orden en que se presentan al editar
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
        (None,                  {'fields': ['user']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently') #Son las columnas que muestra
    list_filter = ['pub_date'] #Agrega una lista de filtros para la fecha
    search_fields = ['question_text'] #Agrega una barra de busqueda del nombre de la pregunta

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user.username
        obj.save()

admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)