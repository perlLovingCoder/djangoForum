from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /thread/5/
    url(r'^(?P<threadID>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<threadID>[0-9]+)/comment/.*', views.detail, name='comment'),
]
