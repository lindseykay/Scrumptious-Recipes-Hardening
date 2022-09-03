# Generated by Django 4.0.3 on 2022-09-02 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_alter_shoppingitem_food_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shopping_item', to='recipes.fooditem', unique=True),
        ),
    ]