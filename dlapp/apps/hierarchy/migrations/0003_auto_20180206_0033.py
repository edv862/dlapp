# Generated by Django 2.0 on 2018-02-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0002_auto_20180203_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchvalues',
            name='part',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='searchvalues',
            name='usage',
            field=models.CharField(max_length=100),
        ),
    ]
