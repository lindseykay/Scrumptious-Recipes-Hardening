# Generated by Django 4.0.3 on 2022-08-31 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='date',
            field=models.DateField(null=True, verbose_name='%B %d, %Y'),
        ),
    ]
