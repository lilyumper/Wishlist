from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^/new$', views.new),
    url(r'^/create$', views.create),
    url(r'^/(?P<id>\d+)/show', views.show),
    url(r'^/(?P<id>\d+)/join$', views.added),
    url(r'^/(?P<id>\d+)/remove$', views.remove),
    url(r'^/(?P<id>\d+)/delete$', views.delete),
    url(r'^/logout$', views.logout)
]
  

