from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Asset, AssetGroup
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
    success_url = reverse_lazy('asset:index')

class GroupView(ListView):
    model = AssetGroup
    template_name = 'asset/grouplist.html'
    context_object_name = 'group_list'
    fields = ['name', 'comment']

class GroupCreateView(CreateView):
    model = AssetGroup
    template_name= 'asset/groupadd.html'
    fields = ['name','comment']
    success_url = reverse_lazy('asset:grouplist')

class GroupDeleteView(DeleteView):
    model = AssetGroup

    success_url = reverse_lazy('asset:grouplist')

class GroupUpdateView(UpdateView):
    model = AssetGroup
    fields = ['name','comment']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('asset:grouplist')