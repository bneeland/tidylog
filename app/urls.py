from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('log/<int:area>/<int:log>', views.Log.as_view(), name='log'),
]
