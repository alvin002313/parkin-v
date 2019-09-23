# Generated by Django 2.2.3 on 2019-09-19 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkplace', '0010_auto_20190918_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('to_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkplace.Place')),
            ],
        ),
    ]
