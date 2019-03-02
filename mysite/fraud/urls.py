from django.conf.urls import url
from fraud import views
app_name = "fraud"

urlpatterns = [
    #url(r'^$', views.front_page, name='front_page'),

    url(r'^index/', views.index, name='index'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^itofficials/', views.itofficials, name='itofficials'),
    url(r'^fraud_list/', views.fraud_list, name='fraud_list'),
    url(r'^new_case/', views.new_case, name='new_case'),


]