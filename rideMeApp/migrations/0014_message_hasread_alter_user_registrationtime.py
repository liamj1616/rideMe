# Generated by Django 4.1.6 on 2023-02-16 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0013_rename_tripsubmitted_posting_submissiontime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='hasRead',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='registrationTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 12, 31, 37, 877428, tzinfo=datetime.timezone.utc)),
        ),
    ]