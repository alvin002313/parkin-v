# Generated by Django 2.2.3 on 2019-09-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkplace', '0012_auto_20190923_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='bronetime_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='bronetime_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
