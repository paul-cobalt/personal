# Generated by Django 2.2.7 on 2019-12-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0005_bestof"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="very_short_description",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
