# Generated by Django 3.0.3 on 2020-07-14 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200713_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acknowledgement',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='tracked',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('UR', 'Unresolved'), ('IP', 'In progress'), ('RE', 'Resolved')], default='UR', max_length=2, null=True),
        ),
    ]
