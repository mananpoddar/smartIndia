from django.conf.urls import url
from . import views 

app_name = 'holidays'

urlpatterns = [
    url(r'^$', views.new_image, name="enter"),
    url(r'^list/$', views.image_process, name="process"),
    # url(r'^applist/$', views.app_victimlist, name="applist")
]
