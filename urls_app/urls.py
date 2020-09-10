from django.urls import path
from . import views

app_name = 'urls_app'

urlpatterns = [
    path('',
         views.urls,
         name='url_list'),
    path('set_interval/',
         views.set_interval,
         name='set_interval'),
    path('get_url_status/',
         views.get_url_status,
         name='get_url_status'),
]
