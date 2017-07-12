from django.conf.urls import url
from . import views
app_name = 'asset'
urlpatterns = [
    url(r'^$', views.index, name='index'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$',views.AssetCreateView.as_view(),name='add'),
    url(r'^grouplist/$',views.GroupView.as_view() ,name='grouplist'),
    url(r'^groupadd/$',views.GroupCreateView.as_view(),name='groupadd'),
    url(r'^(?P<pk>[0-9])+del/$', views.GroupDeleteView.as_view(), name='groupdel'),
    url(r'^(?P<pk>[0-9])+update/$', views.GroupUpdateView.as_view() , name='groupupdate'),
]
