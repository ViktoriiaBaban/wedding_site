# Generated by Django 4.1.7 on 2023-03-19 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wedding", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="guest",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 19, 14, 9, 14, 865375)
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="attend",
            field=models.CharField(
                choices=[("Да", "Да"), ("Нет", "Нет")],
                max_length=20,
                verbose_name="Будет на свадьбе?",
            ),
        ),
    ]