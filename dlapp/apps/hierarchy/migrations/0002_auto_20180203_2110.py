# Generated by Django 2.0 on 2018-02-03 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchvalues',
            old_name='value',
            new_name='part',
        ),
    ]
