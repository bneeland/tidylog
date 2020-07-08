from django.db import models
from django.conf import settings

class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=50)

    FIELD_TYPE_CHOICES = (
        ('CHAR', 'Short text'),
        ('TEXT', 'Long text'),
        ('INT', 'Integer'),
        ('FLOAT', 'Floating point number'),
    )
    type = models.CharField(max_length=5, choices=FIELD_TYPE_CHOICES, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fields = models.ManyToManyField(Field)

    # FIELD_TYPE_CHOICES = (
    #     ('CHAR', 'Short text'),
    #     ('TEXT', 'Long text'),
    #     ('INT', 'Integer'),
    #     ('FLOAT', 'Floating point number'),
    # )
    #
    # field_one_type = models.CharField(max_length=5, choices=FIELD_TYPE_CHOICES, default=None, blank=True, null=True)
    # field_one_name = models.CharField(max_length=50, blank=True, null=True)
    # field_two_type = models.CharField(max_length=5, choices=FIELD_TYPE_CHOICES, default=None, blank=True, null=True)
    # field_two_name = models.CharField(max_length=50, blank=True, null=True)
    # field_three_type = models.CharField(max_length=5, choices=FIELD_TYPE_CHOICES, default=None, blank=True, null=True)
    # field_three_name = models.CharField(max_length=50, blank=True, null=True)
    # field_four_type = models.CharField(max_length=5, choices=FIELD_TYPE_CHOICES, default=None, blank=True, null=True)
    # field_four_name = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Entry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    char_field_one = models.CharField(max_length=50, blank=True, null=True)
    char_field_two = models.CharField(max_length=50, blank=True, null=True)
    char_field_three = models.CharField(max_length=50, blank=True, null=True)

    text_field_one = models.TextField(blank=True, null=True)
    text_field_two = models.TextField(blank=True, null=True)
    text_field_three = models.TextField(blank=True, null=True)

    int_field_one = models.IntegerField(blank=True, null=True)
    int_field_two = models.IntegerField(blank=True, null=True)
    int_field_three = models.IntegerField(blank=True, null=True)

    float_field_one = models.FloatField(blank=True, null=True)
    float_field_two = models.FloatField(blank=True, null=True)
    float_field_three = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.created_at
