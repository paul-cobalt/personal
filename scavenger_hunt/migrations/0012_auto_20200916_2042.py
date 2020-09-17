# Generated by Django 3.0.7 on 2020-09-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0011_location_disable_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='solution',
            field=models.CharField(blank=True, help_text='If provided, the user must input this in order to move on to the next section.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='radius',
            field=models.IntegerField(default=30, help_text="How close the user needs to be in meters to the coordinate in order to advance. This will have no meaning if lat/lng aren't provided."),
        ),
    ]
