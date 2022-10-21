from django.shortcuts import render
from django.views import generic
from .models import Irasas, Komentaras
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class IrasasListView(generic.ListView):
    model = Irasas
    template_name = "irasai.html"
    context_object_name = "irasai"
    paginate_by = 5


class IrasasDetailView(generic.DetailView):
    model = Irasas
    template_name = 'irasas.html'
    context_object_name = 'irasas'


class IrasasCreateView(LoginRequiredMixin, generic.CreateView):
    model = Irasas
    fields = ['pavadinimas', 'tekstas']
    success_url = '/irasai/'
    template_name = 'irasas_form.html'

    def form_valid(self, form):
        form.instance.autorius = self.request.user
        return super().form_valid(form)

class IrasasUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Irasas
    fields = ['pavadinimas', 'tekstas']
    success_url = '/irasai/'
    template_name = 'irasas_form.html'

    def form_valid(self, form):
        form.instance.autorius = self.request.user
        return super().form_valid(form)

    def test_func(self):
        irasas = self.get_object()
        return irasas.autorius == self.request.user
