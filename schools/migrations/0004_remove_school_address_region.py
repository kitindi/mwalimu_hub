# Generated by Django 4.2.1 on 2023-05-16 09:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0003_remove_school_benefits"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school",
            name="address_region",
        ),
    ]