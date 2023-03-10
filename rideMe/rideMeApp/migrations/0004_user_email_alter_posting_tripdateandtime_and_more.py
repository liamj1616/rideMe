# Generated by Django 4.1.6 on 2023-02-11 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0003_posting_tripdateandtime_user_averagerating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='x2019brj@stfx.ca', max_length=254),
        ),
        migrations.AlterField(
            model_name='posting',
            name='tripDateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 17, 36, 28, 336527, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registrationTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 17, 36, 28, 332514, tzinfo=datetime.timezone.utc)),
        ),
    ]
