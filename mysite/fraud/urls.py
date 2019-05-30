from django.conf.urls import url
from fraud import views
app_name = "fraud"

urlpatterns = [
    #url(r'^$', views.front_page, name='front_page'),

    url(r'^index/', views.index, name='index'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^itofficials/', views.itofficials, name='itofficials'),
    url(r'^generate_list/', views.generate_list, name='generate_list'),
    url(r'^new_case/', views.new_case, name='new_case'),
    url(r'^(?P<aadharno>[0-9]+)/', views.generate_report, name='generate_report'),
    url(r'^report_fraud/', views.report_fraud, name='report_fraud'),
    url(r'^lets_see/', views.lets_see, name='lets_see'),



]