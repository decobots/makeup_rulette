# Generated by Django 3.0.5 on 2020-04-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rul', '0016_paletterequest_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='paletterequest',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]