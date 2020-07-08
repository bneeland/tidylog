from django import forms
from django.forms import ModelForm

from . import models

# class CreateEntryForm(ModelForm):
#     class Meta:
#         model = models.Entry
#
#     def __init__(self, area=None, log=None, *args, **kwargs):
#         super(CreateEntryForm, self).__init__(*args, **kwargs)
#         print(area, log)
#     # def __init__(self, *args, **kwargs):
#     #     self.request = kwargs.pop('request', None)
#     #     super(CreateEntryForm, self).__init__(*args, **kwargs)
#     #     print(request_data)
#
#
#         # Get parameters from URL
#         area_pk = area
#         log_pk = log
#         log = models.Log.objects.filter(pk=log_pk)
#         # Get list of fields that pertain to this area and log
#         fields_qs = log.fields # ['position', '...']
#         # Get the field codes
#         field_codes = ['']
#         for field in fields_qs:
#             field_code = models.Field.objects.filter(pk=field)
#             field_codes.append(field_code)
#         # Assign the fields to the form 'fields' variable
#         fields = field_codes
