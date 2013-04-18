from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mysite import views
from tips import views as views2

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^tips/', include('tips.urls')),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^tips/', include ('tips.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit/', views2.submit, name = 'submit'),                  
    url(r'^search/', views2.search, name = 'search'),  
)