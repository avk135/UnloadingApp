# Generated by Django 3.1.3 on 2021-01-26 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0008_client_unloading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unloading',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='UnLoading',
        ),
    ]
