# Generated by Django 5.1 on 2024-08-13 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['sort'], 'verbose_name_plural': 'Staff'},
        ),
    ]
