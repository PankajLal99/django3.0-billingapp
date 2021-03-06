# Generated by Django 3.0.2 on 2020-03-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paresh', '0005_auto_20200318_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='buyer_order_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='challan_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='gst',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
