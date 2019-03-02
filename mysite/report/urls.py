from django.conf.urls import url
from . import views 

app_name = 'report'

urlpatterns = [
    url(r'^$', views.report, name="enter_report"),
    # url(r'^list/$', views.image_process, name="process"),
    # url(r'^applist/$', views.app_victimlist, name="applist")
]
