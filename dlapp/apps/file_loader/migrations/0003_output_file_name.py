# Generated by Django 2.0 on 2018-01-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_loader', '0002_auto_20180127_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='file_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]