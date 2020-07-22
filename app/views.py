from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, resolve
from django.views.generic.base import ContextMixin
from django.utils import timezone
from django.conf import settings
import datetime

from . import models
from . import forms

# Mixins

class AreasMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(AreasMixin, self).get_context_data(**kwargs)
        areas = models.Area.objects.all()
        context['areas'] = areas
        return context

class LogsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(LogsMixin, self).get_context_data(**kwargs)
        area_pk = self.kwargs['area_pk']
        logs = models.Log.objects.filter(area=area_pk)
        context['logs'] = logs
        return context

# Views

class Home(LoginRequiredMixin, AreasMixin, TemplateView):
    login_url = "login"
    template_name = "app/home.html"

class Area(LoginRequiredMixin, AreasMixin, LogsMixin, TemplateView):
    login_url = "login"
    template_name = "app/area.html"

class Log(LoginRequiredMixin, PermissionRequiredMixin, AreasMixin, LogsMixin, CreateView):
    login_url = "login"
    permission_required = 'app.add_entry'
    model = models.Entry
    template_name = "app/log.html"
    form_class = forms.CreateEntryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get area from URL
        area_pk = self.kwargs['area_pk']
        area = models.Area.objects.get(pk=area_pk)
        context['area'] = area

        # Get log from URL
        log_pk = self.kwargs['log_pk']
        log = models.Log.objects.get(pk=log_pk)
        context['log'] = log

        # Get headings for current log
        # Entries
        context['fields'] = log.fields.all()
        # Acknowledgements
        context['unit_lead_acknowledgement_fields'] = log.unit_lead_acknowledgement_fields.all()
        context['superintendent_acknowledgement_fields'] = log.superintendent_acknowledgement_fields.all()
        context['engineering_acknowledgement_fields'] = log.engineering_acknowledgement_fields.all()
        context['new_shift_acknowledgement_fields'] = log.new_shift_acknowledgement_fields.all()

        # Get entries
        entries = models.Entry.objects.filter(log=log).order_by('-created_at')
        # Get acknowledgements
        acknowledgements = models.Acknowledgement.objects.filter(log=log).order_by('-created_at')

        # Filter for daily / date-range views
        url_name = resolve(self.request.path_info).url_name
        context['url_name'] = url_name

        if url_name == "log_daily":
            year = self.kwargs['year']
            month = self.kwargs['month']
            day = self.kwargs['day']

            date = timezone.make_aware(datetime.datetime(year, month, day))

            date_remove = date - datetime.timedelta(days=1)
            date_add = date + datetime.timedelta(days=1)
            context['date_remove'] = date_remove
            context['date_add'] = date_add

            entries = entries.filter(created_at__date=timezone.localtime(date))
            acknowledgements = acknowledgements.filter(created_at__date=timezone.localtime(date))

        if url_name == "log_date_range":
            year_start = self.kwargs['year_start']
            month_start = self.kwargs['month_start']
            day_start = self.kwargs['day_start']
            year_end = self.kwargs['year_end']
            month_end = self.kwargs['month_end']
            day_end = self.kwargs['day_end']

            date_start = timezone.make_aware(datetime.datetime(year_start, month_start, day_start))
            date_end = timezone.make_aware(datetime.datetime(year_end, month_end, day_end))

            entries = entries.filter(
                created_at__gte=timezone.localtime(timezone.localtime(date_start)),
                created_at__lt=timezone.localtime(timezone.localtime(date_end)),
            )
            acknowledgements = acknowledgements.filter(
                created_at__gte=timezone.localtime(timezone.localtime(date_start)),
                created_at__lt=timezone.localtime(timezone.localtime(date_end)),
            )

        context['entries'] = entries

        # Filter acknowledgements by group
        context['unit_lead_acknowledgements'] = acknowledgements.filter(group__name="Unit lead")
        context['superintendent_acknowledgements'] = acknowledgements.filter(group__name="Superintendent")
        context['engineering_acknowledgements'] = acknowledgements.filter(group__name="Engineering")
        context['new_shift_acknowledgements'] = acknowledgements.filter(group__name="Operator")
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'log_pk': self.kwargs['log_pk'],
        })
        return kwargs

    def get_success_url(self):
        url_name = resolve(self.request.path_info).url_name
        url_name_complete = 'app:'+url_name

        if url_name == 'log':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
            })
        elif url_name == 'log_daily':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year': self.kwargs['year'],
                'month': self.kwargs['month'],
                'day': self.kwargs['day'],
            })
        elif url_name == 'log_date_range':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year_start': self.kwargs['year_start'],
                'month_start': self.kwargs['month_start'],
                'day_start': self.kwargs['day_start'],
                'year_end': self.kwargs['year_end'],
                'month_end': self.kwargs['month_end'],
                'day_end': self.kwargs['day_end'],
            })

class Entry(LoginRequiredMixin, PermissionRequiredMixin, AreasMixin, LogsMixin, TemplateView):
    login_url = "login"
    permission_required = 'app.view_entry'
    template_name = "app/entry.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get area from URL
        area_pk = self.kwargs['area_pk']
        area = models.Area.objects.get(pk=area_pk)
        context['area'] = area

        # Get log from URL
        log_pk = self.kwargs['log_pk']
        log = models.Log.objects.get(pk=log_pk)
        context['log'] = log

        # Get headings for current log
        context['fields'] = log.fields.all()

        # Get entry from URL
        entry_pk = self.kwargs['entry_pk']
        context['entry'] = models.Entry.objects.get(pk=entry_pk)

        return context
