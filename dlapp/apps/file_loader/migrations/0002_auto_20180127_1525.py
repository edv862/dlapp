# Generated by Django 2.0 on 2018-01-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_loader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='search_type',
            field=models.IntegerField(choices=[(0, 'Text Search'), (1, 'Line Search'), (2, 'Paragraph Search')], default=0),
        ),
        migrations.AddField(
            model_name='output',
            name='search_value',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
