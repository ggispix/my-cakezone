# Generated by Django 5.1 on 2024-08-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_category_options_alter_dish_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(upload_to='dish/'),
        ),
    ]
