# Generated by Django 3.0.5 on 2020-04-15 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='operationType',
        ),
        migrations.RemoveField(
            model_name='delete',
            name='operationType',
        ),
        migrations.RemoveField(
            model_name='download',
            name='operationType',
        ),
        migrations.RemoveField(
            model_name='move',
            name='operationType',
        ),
        migrations.RemoveField(
            model_name='rename',
            name='operationType',
        ),
    ]