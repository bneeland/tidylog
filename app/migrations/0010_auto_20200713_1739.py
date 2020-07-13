# Generated by Django 3.0.3 on 2020-07-13 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('app', '0009_auto_20200711_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='engineering_acknowledgement_fields',
            field=models.ManyToManyField(blank=True, related_name='engineering_acknowledgement_fields', to='app.Field'),
        ),
        migrations.AddField(
            model_name='log',
            name='new_shift_acknowledgement_fields',
            field=models.ManyToManyField(blank=True, related_name='new_shift_acknowledgement_fields', to='app.Field'),
        ),
        migrations.AddField(
            model_name='log',
            name='superintendent_acknowledgement_fields',
            field=models.ManyToManyField(blank=True, related_name='superintendent_acknowledgement_fields', to='app.Field'),
        ),
        migrations.AddField(
            model_name='log',
            name='unit_lead_acknowledgement_fields',
            field=models.ManyToManyField(blank=True, related_name='unit_lead_acknowledgement_fields', to='app.Field'),
        ),
        migrations.CreateModel(
            name='Acknowledgement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('CF1', models.CharField(blank=True, max_length=50, null=True)),
                ('CF2', models.CharField(blank=True, max_length=50, null=True)),
                ('TF1', models.TextField(blank=True, null=True)),
                ('TF2', models.TextField(blank=True, null=True)),
                ('IF1', models.IntegerField(blank=True, null=True)),
                ('IF2', models.IntegerField(blank=True, null=True)),
                ('FF1', models.FloatField(blank=True, null=True)),
                ('FF2', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Log')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
