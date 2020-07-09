from django.db import models
from django.conf import settings

class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Field(models.Model):
    name = models.CharField(max_length=50)
    FIELD_BANK = (
        ('CF1', 'Short text field 1'),
        ('CF2', 'Short text field 2'),
        ('TF1', 'Long text field 1'),
        ('TF2', 'Long text field 2'),
        ('IF1', 'Integer field 1'),
        ('IF2', 'Integer field 2'),
        ('FF1', 'Floating point number field 1'),
        ('FF2', 'Floating point number field 2'),
    )
    type = models.CharField(max_length=3, choices=FIELD_BANK, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fields = models.ManyToManyField(Field)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Entry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CF1 = models.CharField(max_length=50, blank=True, null=True)
    CF2 = models.CharField(max_length=50, blank=True, null=True)

    TF1 = models.TextField(blank=True, null=True)
    TF2 = models.TextField(blank=True, null=True)

    IF1 = models.IntegerField(blank=True, null=True)
    IF2 = models.IntegerField(blank=True, null=True)

    FF1 = models.FloatField(blank=True, null=True)
    FF2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name_plural = "entries"
