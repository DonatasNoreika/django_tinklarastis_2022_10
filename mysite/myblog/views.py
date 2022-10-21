from django.shortcuts import render
from django.views import generic
from .models import Irasas, Komentaras

# Create your views here.

class IrasasListView(generic.ListView):
    model = Irasas
    template_name = "irasai.html"
    context_object_name = "irasai"
    paginate_by = 5
