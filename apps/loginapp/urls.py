from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^success$',views.success),
    url(r'^login$', views.login)
    
]
