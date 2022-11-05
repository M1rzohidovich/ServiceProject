# Generated by Django 4.1.2 on 2022-11-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_ichkimijoz_options_alter_tashqimijoz_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ichkimijoz',
            name='passport_seria',
        ),
        migrations.RemoveField(
            model_name='tashqimijoz',
            name='passport_seria',
        ),
        migrations.AddField(
            model_name='ichkimijoz',
            name='address',
            field=models.CharField(default='default value null', max_length=180),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tashqimijoz',
            name='address',
            field=models.CharField(default='null', max_length=180),
            preserve_default=False,
        ),
    ]