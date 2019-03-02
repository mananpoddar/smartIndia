from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^fraud/', include("fraud.urls" , namespace="fraud")),#managefraudroute
]

    