# Generated by Django 3.0.8 on 2020-07-08 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('field_one_name', models.CharField(blank=True, max_length=50, null=True)),
                ('field_two_name', models.CharField(blank=True, max_length=50, null=True)),
                ('field_three_name', models.CharField(blank=True, max_length=50, null=True)),
                ('field_four_name', models.CharField(blank=True, max_length=50, null=True)),
                ('field_one_type', models.CharField(blank=True, choices=[('CHAR', 'Short text'), ('TEXT', 'Long text'), ('INT', 'Integer'), ('FLOAT', 'Floating point number')], default=None, max_length=5, null=True)),
                ('field_two_type', models.CharField(blank=True, choices=[('CHAR', 'Short text'), ('TEXT', 'Long text'), ('INT', 'Integer'), ('FLOAT', 'Floating point number')], default=None, max_length=5, null=True)),
                ('field_three_type', models.CharField(blank=True, choices=[('CHAR', 'Short text'), ('TEXT', 'Long text'), ('INT', 'Integer'), ('FLOAT', 'Floating point number')], default=None, max_length=5, null=True)),
                ('field_four_type', models.CharField(blank=True, choices=[('CHAR', 'Short text'), ('TEXT', 'Long text'), ('INT', 'Integer'), ('FLOAT', 'Floating point number')], default=None, max_length=5, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('char_field_one', models.CharField(blank=True, max_length=50, null=True)),
                ('char_field_two', models.CharField(blank=True, max_length=50, null=True)),
                ('char_field_three', models.CharField(blank=True, max_length=50, null=True)),
                ('text_field_one', models.TextField(blank=True, null=True)),
                ('text_field_two', models.TextField(blank=True, null=True)),
                ('text_field_three', models.TextField(blank=True, null=True)),
                ('int_field_one', models.IntegerField(blank=True, null=True)),
                ('int_field_two', models.IntegerField(blank=True, null=True)),
                ('int_field_three', models.IntegerField(blank=True, null=True)),
                ('float_field_one', models.FloatField(blank=True, null=True)),
                ('float_field_two', models.FloatField(blank=True, null=True)),
                ('float_field_three', models.FloatField(blank=True, null=True)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Log')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
