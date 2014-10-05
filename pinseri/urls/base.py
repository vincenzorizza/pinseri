from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from solid_i18n.urls import solid_i18n_patterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

# without i18n
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^thirdauth/$', TemplateView.as_view(template_name='thirdauth/home.html'), name='home'),
    url(r'^complete/facebook/$', TemplateView.as_view(template_name='thirdauth/logged.html'), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    (r'^i18n/', include('django.conf.urls.i18n')),
    #COMPRESS_URL = r'%s/static' % os.path.abspath(os.path.dirname(__file__))

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),

    url(r'^prova/lang/', TemplateView.as_view(template_name='language.html'), name='lang'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
   )
urlpatterns += staticfiles_urlpatterns()

urlpatterns += solid_i18n_patterns('',
    # Home Page -- Replace as you prefer
    url(r'^$', TemplateView.as_view(template_name='comingsoon.html'), name='home'),
    url(r'^prova/$', TemplateView.as_view(template_name='home.html'), name='prova'),
    url(r'^prova/product/$', TemplateView.as_view(template_name='product.html'), name='product'),
    url(r'^prova/service/$', TemplateView.as_view(template_name='service.html'), name='service'),
    url(r'^prova/order/$', TemplateView.as_view(template_name='order.html'), name='order'),
    url(r'^prova/contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^prova/about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^soon/', TemplateView.as_view(template_name='comingsoon.html'), name='home'),
)