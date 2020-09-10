from django.urls import path
from . import views

app_name = 'urls_app'

urlpatterns = [
    path('',
         views.urls,
         name='url_list'),
]
