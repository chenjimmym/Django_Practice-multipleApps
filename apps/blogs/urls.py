from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<blog_number>\d+)/edit', views.edit),
    url(r'^(?P<blog_number>\d+)/delete', views.destroy),
    url(r'^(?P<blog_number>\d+)', views.show)
]