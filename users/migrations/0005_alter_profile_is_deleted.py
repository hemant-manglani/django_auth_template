# Generated by Django 5.0 on 2023-12-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_profile_is_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
