from django.urls import path
from authentication.views import *

app_name = 'authentication'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('home/', login_redirect, name='home'),
    path('zone/add/', zone_add, name='zoneadd'),
    path('zone/list/', zone_list, name='zonelist'),
    path('user/add/', user_add, name='useradd'),
    path('wereda/add/', wereda_add, name='weredaadd'),
    path('kebele/add/', kebele_add, name='kebeleadd'),
    path('user_exel/', user_exel, name='user-exel'),
]
