from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('area-<int:area_pk>', views.Area.as_view(), name='area'),
    path('area-<int:area_pk>/log-<int:log_pk>', views.Log.as_view(), name='log'),
]
