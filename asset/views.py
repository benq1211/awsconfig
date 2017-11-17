from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Asset
# Create your views here.
class IndexView(ListView):
    model = Asset
    template_name = 'asset/index.html'
    context_object_name = 'asset_list'
    fields = ['ip', 'hostname','env','cpu','memory','disk']



class AssetCreateView(CreateView):
    model =Asset
    template_name= 'asset/add.html'
    fields = ['hostname','ip','port','username','password','use_default_auth','is_active']

