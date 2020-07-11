from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('area-<int:area_pk>', views.Area.as_view(), name='area'),
    path('area-<int:area_pk>/log-<int:log_pk>', views.Log.as_view(), name='log'),
    path('area-<int:area_pk>/log-<int:log_pk>/1-day/<int:year>-<int:month>-<int:day>', views.Log.as_view(), name='log_1_day'),
    path('area-<int:area_pk>/log-<int:log_pk>/date-range/<int:year_start>-<int:month_start>-<int:day_start>/<int:year_end>-<int:month_end>-<int:day_end>', views.Log.as_view(), name='log_date_range'),
]
