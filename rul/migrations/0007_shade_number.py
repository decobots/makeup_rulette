# Generated by Django 3.0.5 on 2020-04-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rul', '0006_shade_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='shade',
            name='number',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
