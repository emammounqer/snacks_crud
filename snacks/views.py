from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Snack
# Create your views here.


class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'create_snack.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
