# Generated by Django 5.0.4 on 2024-05-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FacultyView", "0003_alter_uniqueid_unique_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uniqueid",
            name="unique_id",
            field=models.CharField(
                default="LjtxpcknIz3UvFb4R4KOHlKvViHRvFoW", max_length=32
            ),
        ),
    ]