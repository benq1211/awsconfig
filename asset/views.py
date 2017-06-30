from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Asset
# Create your views here.
class IndexView(ListView):
    model = Asset
    template_name = 'asset/index.html'
    context_object_name = 'asset_list'
    fields = ['ip', 'hostname', 'group','env','cpu','memory','disk']



