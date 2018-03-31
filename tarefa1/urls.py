from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^olamundo/$', views.olamundo, name='olamundo'),
    url(r'^somatorio/$', views.somatorio, name='somatorio'),

]