from django.conf.urls import patterns, url
from . import views
# for django 1.9 use from . import views
urlpatterns = patterns('',
  url(r'^$', views.start, name='start'),
  url(r'^postDirector/$', views.postDirector, name='postDirector'),
  url(r'^startPost/$', views.start.startPost, name='startPost'),
  url(r'^mountains/$', views.mountains, name='mountains'),
  url(r'^mountainsPost/$', views.mountainsPost, name='mountainsPost')
  
)