# Generated by Django 3.0.2 on 2020-03-19 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paresh', '0006_auto_20200319_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='products',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='products',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='products',
            name='total',
        ),
        migrations.RemoveField(
            model_name='products',
            name='words',
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('sub_total', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('words', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paresh.Products')),
            ],
        ),
    ]