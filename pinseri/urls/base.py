from django.conf.urls import *
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Home Page -- Replace as you prefer
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thirdauth/$', TemplateView.as_view(template_name='thirdauth/home.html'), name='home'),
    url(r'^complete/facebook/$', TemplateView.as_view(template_name='thirdauth/logged.html'), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
