from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fraud/', include("fraud.urls" , namespace="fraud")),#managefraudroute
    url(r'^holidays/', include("holidays.urls" , namespace="holidays")), #for using holiday images
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)