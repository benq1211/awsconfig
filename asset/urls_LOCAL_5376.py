from django.conf.urls import url
from . import views
app_name = 'asset'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.AssetCreateView.as_view(), name='add'),
]
