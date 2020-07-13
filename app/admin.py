from django.contrib import admin

from . import models

admin.site.register(models.Area)
admin.site.register(models.Log)
admin.site.register(models.Field)
admin.site.register(models.Category)
admin.site.register(models.Entry)
admin.site.register(models.Acknowledgement)
