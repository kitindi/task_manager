# Generated by Django 5.0.2 on 2024-03-02 21:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_userprofile_date_of_birth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="city_name",
        ),
    ]