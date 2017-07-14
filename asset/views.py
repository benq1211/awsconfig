from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

import boto3

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Asset, AssetGroup
# Create your views here.

def index(request):
    asset_list = Asset.objects.all()

    return render(request,'asset/index.html',{'asset_list':asset_list})

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

class AssetDeleteView(DeleteView):
    model = Asset

    success_url = reverse_lazy('asset:index')


def AssetUpdateByAws(request,pk):

    ec2 = boto3.resource('ec2')
    asset = get_object_or_404(Asset, id=pk)

    instance = ec2.Instance(asset.instance)

    try:

        asset.ip =  instance.public_ip_address
        print(instance.public_ip_address)
        asset.instance_type= instance.instance_type
        asset.instance_status = instance.state['Name']
        print(asset.instance_status)
        asset.security_group = instance.security_groups[0]['GroupName']
        asset.save()
    except Exception as e:

        return redirect(reverse('asset:index'))
     #

    return redirect(reverse('asset:index'))

class AssetUpdateView(UpdateView):
    model = Asset
   # fields = ['name','comment']
    fields = '__all__'
    template_name_suffix = '_update_form'
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