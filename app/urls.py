from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('log/<int:area_pk>/<int:log_pk>', views.Log.as_view(), name='log'),
]
