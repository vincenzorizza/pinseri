from django.conf.urls.static import static

from pinseri.urls.base import *

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)