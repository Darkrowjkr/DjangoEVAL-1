from django.views import generic

class HomeView(generic.ListView):
    template_name = 'admin/home.html'

    def get_queryset(self):
        pass