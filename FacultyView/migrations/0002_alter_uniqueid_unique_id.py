# Generated by Django 5.0.4 on 2024-05-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FacultyView", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uniqueid",
            name="unique_id",
            field=models.CharField(
                default="yxkqCzlex1Bt4g33QPBQ90NJ78cRGlqr", max_length=32
            ),
        ),
    ]
