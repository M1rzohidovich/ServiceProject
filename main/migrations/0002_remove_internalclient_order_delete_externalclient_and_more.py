# Generated by Django 4.1.2 on 2022-10-30 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internalclient',
            name='order',
        ),
        migrations.DeleteModel(
            name='ExternalClient',
        ),
        migrations.DeleteModel(
            name='InternalClient',
        ),
    ]
