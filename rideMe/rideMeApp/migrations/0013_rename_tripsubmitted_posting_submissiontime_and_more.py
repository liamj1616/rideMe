# Generated by Django 4.1.6 on 2023-02-15 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0012_rename_tripdateandtime_posting_tripsubmitted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='tripSubmitted',
            new_name='submissionTime',
        ),
        migrations.AlterField(
            model_name='user',
            name='registrationTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 21, 38, 21, 565049, tzinfo=datetime.timezone.utc)),
        ),
    ]