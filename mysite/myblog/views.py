from django.shortcuts import render, reverse
from django.views import generic
from .models import Irasas, Komentaras
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import KomentarasForm
# Create your views here.

class IrasasListView(generic.ListView):
    model = Irasas
    template_name = "irasai.html"
    context_object_name = "irasai"
    paginate_by = 5


class IrasasDetailView(FormMixin, generic.DetailView):
    model = Irasas
    template_name = 'irasas.html'
    context_object_name = 'irasas'
    form_class = KomentarasForm

    # def get_context_data(self, *args, **kwargs):
    #     context = super(IrasasDetailView, self).get_context_data(**kwargs)
    #     context['form'] = KomentarasForm(initial={'straipsnis': self.object, "autorius": self.request.user})
    #     return context

    def get_success_url(self):
        return reverse("irasas", kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(form.is_valid())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.irasas = self.object
        form.instance.autorius = self.request.user
        form.save()
        return super().form_valid(form)


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


class IrasasDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Irasas
    success_url = '/irasai/'
    template_name = "irasas_delete.html"
    context_object_name = 'irasas'

    def test_func(self):
        irasas = self.get_object()
        return irasas.autorius == self.request.user