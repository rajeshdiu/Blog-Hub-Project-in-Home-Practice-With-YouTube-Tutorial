# Generated by Django 5.1.2 on 2024-10-19 13:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0004_alter_customuser_user_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPostModel",
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
                ("BlogTitle", models.CharField(max_length=500, null=True)),
                ("BlogBody", models.TextField(null=True)),
                (
                    "Category",
                    models.CharField(
                        choices=[
                            ("Technology", "Technology"),
                            ("Sports", "Sports"),
                            ("Entertainment", "Entertainment"),
                            ("Politics", "Politics"),
                            ("Business", "Business"),
                            ("Health", "Health"),
                            ("Education", "Education"),
                            ("Travel", "Travel"),
                            ("Food", "Food"),
                            ("Fashion", "Fashion"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("Blog_Pic", models.ImageField(null=True, upload_to="Media/Blog_Pic")),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
