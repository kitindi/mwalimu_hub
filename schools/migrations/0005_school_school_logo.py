# Generated by Django 4.2 on 2023-05-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0004_alter_job_options_alter_school_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="school",
            name="school_logo",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
    ]
