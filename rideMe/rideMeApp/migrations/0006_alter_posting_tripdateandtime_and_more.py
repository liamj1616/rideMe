# Generated by Django 4.1.6 on 2023-02-11 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0005_alter_posting_tripdateandtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='tripDateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 17, 38, 24, 322161, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registrationTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 17, 38, 24, 322161, tzinfo=datetime.timezone.utc)),
        ),
    ]
