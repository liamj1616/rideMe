# Generated by Django 4.1.6 on 2023-03-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideMeApp', '0028_alter_usersinteractedforusers_postingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='securityQuestion',
            field=models.CharField(default='What is the name of the site', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='securityQuestionAnswer',
            field=models.CharField(default='rideMe', max_length=50),
        ),
    ]
