from django.shortcuts import render
from django.views.generic import ListView
from .models import Snack
# Create your views here.


class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks'
