# Generated by Django 3.0.7 on 2020-11-17 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_datapoint_response_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expire_message_after',
            field=models.DurationField(default=datetime.timedelta(0, 900)),
        ),
    ]