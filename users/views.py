from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from users.models import Person


class PersonListView(TemplateView):
    model = Person
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        return context
