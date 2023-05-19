# Generated by Django 4.2.1 on 2023-05-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="benefits",
            field=models.CharField(
                choices=[
                    ("PB", "Parent Benefits"),
                    ("WB", "Work Benefits"),
                    ("VT", "vacation time Off"),
                    ("FR", "Financial and Retirements Benefits"),
                    ("OP", "Office Life and Perks"),
                    ("PD", "professional Development"),
                ],
                max_length=225,
            ),
        ),
        migrations.AlterField(
            model_name="school",
            name="category",
            field=models.CharField(
                choices=[
                    ("TZ", "NECTA School"),
                    ("UK", "Cambridge International School"),
                    ("IB", "International Baccalaureate® (IB)"),
                ],
                max_length=255,
            ),
        ),
    ]