# Generated by Django 4.2.2 on 2023-06-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='carbs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='fats',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
