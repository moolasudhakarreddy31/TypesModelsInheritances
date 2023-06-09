# Generated by Django 4.2 on 2023-04-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("modelsapp", "0002_contactinfo1_studentinfo1_teacharsinfo1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parent",
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
                ("fd1", models.CharField(max_length=222)),
                ("fd2", models.CharField(max_length=222)),
            ],
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "parent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="modelsapp.parent",
                    ),
                ),
                ("fd3", models.CharField(max_length=222)),
                ("fd4", models.CharField(max_length=222)),
            ],
            bases=("modelsapp.parent",),
        ),
        migrations.CreateModel(
            name="SubChild",
            fields=[
                (
                    "child_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="modelsapp.child",
                    ),
                ),
                ("fd5", models.CharField(max_length=222)),
            ],
            bases=("modelsapp.child",),
        ),
    ]
