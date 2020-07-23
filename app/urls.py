from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('area-<int:area_pk>', views.Area.as_view(), name='area'),
    path('area-<int:area_pk>/log-<int:log_pk>/acknowledgements', views.Log.as_view(), name='log', kwargs={'acknowledgements': True}),
    path('area-<int:area_pk>/log-<int:log_pk>', views.Log.as_view(), name='log', kwargs={'acknowledgements': False}),
    path('area-<int:area_pk>/log-<int:log_pk>/daily/<int:year>-<int:month>-<int:day>/acknowledgements', views.Log.as_view(), name='log_daily', kwargs={'acknowledgements': True}),
    path('area-<int:area_pk>/log-<int:log_pk>/daily/<int:year>-<int:month>-<int:day>', views.Log.as_view(), name='log_daily', kwargs={'acknowledgements': False}),
    path('area-<int:area_pk>/log-<int:log_pk>/date-range/<int:year_start>-<int:month_start>-<int:day_start>/<int:year_end>-<int:month_end>-<int:day_end>/acknowledgements', views.Log.as_view(), name='log_date_range', kwargs={'acknowledgements': True}),
    path('area-<int:area_pk>/log-<int:log_pk>/date-range/<int:year_start>-<int:month_start>-<int:day_start>/<int:year_end>-<int:month_end>-<int:day_end>', views.Log.as_view(), name='log_date_range', kwargs={'acknowledgements': False}),
    path('area-<int:area_pk>/log-<int:log_pk>/entry-<int:entry_pk>', views.Entry.as_view(), name='entry'),
    path('area-<int:area_pk>/log-<int:log_pk>/daily/<int:year>-<int:month>-<int:day>/entry-<int:entry_pk>', views.Entry.as_view(), name='entry_daily'),
    path('area-<int:area_pk>/log-<int:log_pk>/entry-<int:entry_pk>/status', views.Status.as_view(), name='status'),
    path('area-<int:area_pk>/log-<int:log_pk>/daily/<int:year>-<int:month>-<int:day>/entry-<int:entry_pk>/status', views.Status.as_view(), name='status_daily'),
]
