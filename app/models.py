from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=50)
    FIELD_BANK = (
        ('CF1', 'Short text field 1'),
        ('CF2', 'Short text field 2'),
        ('CF3', 'Short text field 3'),
        ('CF4', 'Short text field 4'),
        ('CF5', 'Short text field 5'),
        ('CF6', 'Short text field 6'),
        ('CF7', 'Short text field 7'),
        ('CF8', 'Short text field 8'),
        ('CF9', 'Short text field 9'),
        ('CF10', 'Short text field 10'),
        ('TF1', 'Long text field 1'),
        ('TF2', 'Long text field 2'),
        ('TF3', 'Long text field 3'),
        ('TF4', 'Long text field 4'),
        ('TF5', 'Long text field 5'),
        ('TF6', 'Long text field 5'),
        ('TF7', 'Long text field 5'),
        ('TF8', 'Long text field 5'),
        ('TF9', 'Long text field 5'),
        ('TF10', 'Long text field 5'),
        ('IF1', 'Integer field 1'),
        ('IF2', 'Integer field 2'),
        ('IF3', 'Integer field 3'),
        ('IF4', 'Integer field 4'),
        ('IF5', 'Integer field 5'),
        ('FF1', 'Floating point number field 1'),
        ('FF2', 'Floating point number field 2'),
        ('FF3', 'Floating point number field 3'),
        ('FF4', 'Floating point number field 4'),
        ('FF5', 'Floating point number field 5'),
    )
    type = models.CharField(max_length=5, choices=FIELD_BANK, default=None, blank=True, null=True)
    shown_in_table = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AcknowledgementField(models.Model):
    name = models.CharField(max_length=50)
    FIELD_BANK = (
        ('CF1', 'Short text field 1'),
        ('CF2', 'Short text field 2'),
        ('CF3', 'Short text field 3'),
        ('CF4', 'Short text field 4'),
        ('CF5', 'Short text field 5'),
        ('CF6', 'Short text field 6'),
        ('CF7', 'Short text field 7'),
        ('CF8', 'Short text field 8'),
        ('CF9', 'Short text field 9'),
        ('CF10', 'Short text field 10'),
        ('TF1', 'Long text field 1'),
        ('TF2', 'Long text field 2'),
        ('TF3', 'Long text field 3'),
        ('TF4', 'Long text field 4'),
        ('TF5', 'Long text field 5'),
        ('TF6', 'Long text field 6'),
        ('TF7', 'Long text field 7'),
        ('TF8', 'Long text field 8'),
        ('TF9', 'Long text field 9'),
        ('TF10', 'Long text field 10'),
        ('IF1', 'Integer field 1'),
        ('IF2', 'Integer field 2'),
        ('IF3', 'Integer field 3'),
        ('IF4', 'Integer field 4'),
        ('IF5', 'Integer field 5'),
        ('FF1', 'Floating point number field 1'),
        ('FF2', 'Floating point number field 2'),
        ('FF3', 'Floating point number field 3'),
        ('FF4', 'Floating point number field 4'),
        ('FF5', 'Floating point number field 5'),
    )
    type = models.CharField(max_length=5, choices=FIELD_BANK, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fields = models.ManyToManyField(Field, blank=True)
    unit_lead_acknowledgement_fields = models.ManyToManyField(AcknowledgementField, blank=True, related_name='unit_lead_acknowledgement_fields')
    superintendent_acknowledgement_fields = models.ManyToManyField(AcknowledgementField, blank=True, related_name='superintendent_acknowledgement_fields')
    engineering_acknowledgement_fields = models.ManyToManyField(AcknowledgementField, blank=True, related_name='engineering_acknowledgement_fields')
    new_shift_acknowledgement_fields = models.ManyToManyField(AcknowledgementField, blank=True, related_name='new_shift_acknowledgement_fields')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_tracked = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Entry(models.Model):
    STATUS_BANK = (
        ('UR', 'Unresolved'),
        ('IP', 'In progress'),
        ('RE', 'Resolved'),
        ('AP', 'Approved'),
        ('CA', 'Cancelled'),
    )
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_BANK, default='None', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CF1 = models.CharField(max_length=50, blank=True, null=True)
    CF2 = models.CharField(max_length=50, blank=True, null=True)
    CF3 = models.CharField(max_length=50, blank=True, null=True)
    CF4 = models.CharField(max_length=50, blank=True, null=True)
    CF5 = models.CharField(max_length=50, blank=True, null=True)
    CF6 = models.CharField(max_length=50, blank=True, null=True)
    CF7 = models.CharField(max_length=50, blank=True, null=True)
    CF8 = models.CharField(max_length=50, blank=True, null=True)
    CF9 = models.CharField(max_length=50, blank=True, null=True)
    CF10 = models.CharField(max_length=50, blank=True, null=True)

    TF1 = models.TextField(blank=True, null=True)
    TF2 = models.TextField(blank=True, null=True)
    TF3 = models.TextField(blank=True, null=True)
    TF4 = models.TextField(blank=True, null=True)
    TF5 = models.TextField(blank=True, null=True)
    TF6 = models.TextField(blank=True, null=True)
    TF7 = models.TextField(blank=True, null=True)
    TF8 = models.TextField(blank=True, null=True)
    TF9 = models.TextField(blank=True, null=True)
    TF10 = models.TextField(blank=True, null=True)

    IF1 = models.IntegerField(blank=True, null=True)
    IF2 = models.IntegerField(blank=True, null=True)
    IF3 = models.IntegerField(blank=True, null=True)
    IF4 = models.IntegerField(blank=True, null=True)
    IF5 = models.IntegerField(blank=True, null=True)

    FF1 = models.FloatField(blank=True, null=True)
    FF2 = models.FloatField(blank=True, null=True)
    FF3 = models.FloatField(blank=True, null=True)
    FF4 = models.FloatField(blank=True, null=True)
    FF5 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name_plural = "entries"

class Acknowledgement(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    for_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CF1 = models.CharField(max_length=50, blank=True, null=True)
    CF2 = models.CharField(max_length=50, blank=True, null=True)
    CF3 = models.CharField(max_length=50, blank=True, null=True)
    CF4 = models.CharField(max_length=50, blank=True, null=True)
    CF5 = models.CharField(max_length=50, blank=True, null=True)
    CF6 = models.CharField(max_length=50, blank=True, null=True)
    CF7 = models.CharField(max_length=50, blank=True, null=True)
    CF8 = models.CharField(max_length=50, blank=True, null=True)
    CF9 = models.CharField(max_length=50, blank=True, null=True)
    CF10 = models.CharField(max_length=50, blank=True, null=True)

    TF1 = models.TextField(blank=True, null=True)
    TF2 = models.TextField(blank=True, null=True)
    TF3 = models.TextField(blank=True, null=True)
    TF4 = models.TextField(blank=True, null=True)
    TF5 = models.TextField(blank=True, null=True)
    TF6 = models.TextField(blank=True, null=True)
    TF7 = models.TextField(blank=True, null=True)
    TF8 = models.TextField(blank=True, null=True)
    TF9 = models.TextField(blank=True, null=True)
    TF10 = models.TextField(blank=True, null=True)

    IF1 = models.IntegerField(blank=True, null=True)
    IF2 = models.IntegerField(blank=True, null=True)
    IF3 = models.IntegerField(blank=True, null=True)
    IF4 = models.IntegerField(blank=True, null=True)
    IF5 = models.IntegerField(blank=True, null=True)

    FF1 = models.FloatField(blank=True, null=True)
    FF2 = models.FloatField(blank=True, null=True)
    FF3 = models.FloatField(blank=True, null=True)
    FF4 = models.FloatField(blank=True, null=True)
    FF5 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.for_date)
