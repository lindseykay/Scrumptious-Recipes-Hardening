# Generated by Django 4.0.3 on 2022-09-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_alter_shoppingitem_food_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
