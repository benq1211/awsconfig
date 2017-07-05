from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Asset
# Create your views here.
class IndexView(ListView):
    model = Asset
    template_name = 'asset/index.html'
    context_object_name = 'asset_list'
    fields = ['ip', 'hostname', 'group','env','cpu','memory','disk']



class AssetCreateView(CreateView):
    model =Asset
    template_name= 'asset/add.html'
    fields = ['hostname','ip','port','group','username','password','use_default_auth','is_active']