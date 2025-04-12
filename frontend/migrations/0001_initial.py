# Generated by Django 4.2.19 on 2025-04-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "location",
                    models.CharField(
                        choices=[("온라인", "온라인"), ("오프라인", "오프라인")],
                        max_length=100,
                    ),
                ),
                ("region", models.CharField(blank=True, max_length=100)),
                ("price", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
