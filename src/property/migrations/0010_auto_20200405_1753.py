# Generated by Django 3.0.5 on 2020-04-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20200405_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]