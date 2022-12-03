# Generated by Django 4.1.3 on 2022-12-03 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("pseudonym", models.CharField(blank=True, max_length=64, null=True)),
                ("age", models.IntegerField()),
                ("retired", models.BooleanField()),
            ],
        ),
    ]
