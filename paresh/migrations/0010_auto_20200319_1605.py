# Generated by Django 3.0.2 on 2020-03-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paresh', '0009_auto_20200319_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='discount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='amount',
            name='gst',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='amount',
            name='sub_total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='amount',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
