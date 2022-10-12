# Generated by Django 4.1.2 on 2022-10-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="credentials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("database", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("port", models.CharField(max_length=100)),
            ],
        ),
    ]