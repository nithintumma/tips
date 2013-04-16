from django.conf.urls import patterns, url

from tips import views

urlpatterns = patterns('',
    url(r'^$', views.reviews, name='reviews')
)

