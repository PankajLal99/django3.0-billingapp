# Generated by Django 3.0.2 on 2020-03-19 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caltesting', '0017_auto_20200319_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal',
            name='num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caltesting.Invoi'),
        ),
    ]
