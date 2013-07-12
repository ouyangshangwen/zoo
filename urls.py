from django.conf.urls.defaults import *
from zoo.myzoo import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^zoo/', include('zoo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^accounts/register/$',views.resgister),
    (r'^gravatar/$',views.gravatar),
    (r'^login/$',views.login),
    (r'^index/$',views.printx),
    (r'^$',views.login),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/yu/zoo/static/js'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/yu/zoo/static/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/yu/zoo/static/images'}),
)
