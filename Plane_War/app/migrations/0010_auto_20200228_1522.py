# Generated by Django 3.0.3 on 2020-02-28 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_developer_bullets_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planes',
            name='map_ps_left',
        ),
        migrations.RemoveField(
            model_name='planes',
            name='map_ps_top',
        ),
    ]