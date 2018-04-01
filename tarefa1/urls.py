from django.conf.urls import url

from tarefa1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^olamundo/$', views.olamundo, name='olamundo'),
    url(r'^lembretes/guarda-lembrete', views.guarda_lembrete, name='guarda_lembrete'),
    url(r'^lembretes/$', views.lembretes, name='lembretes'),
    url(r'^lembretes/(?P<username>[\w-]+)/$', views.lembretes, name='lembretes'),
    url(r'^somatorio/$', views.somatorio, name='somatorio'),
    url(r'^mostraheader/$', views.mostraheader, name='mostraheader'),
]
