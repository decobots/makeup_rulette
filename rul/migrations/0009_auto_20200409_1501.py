# Generated by Django 3.0.5 on 2020-04-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rul', '0008_auto_20200406_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shade',
            name='color',
            field=models.CharField(choices=[('P', 'Pinc'), ('Co', 'Corall'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('C', 'Cyan'), ('V', 'Violet'), ('B', 'Black'), ('Br', 'Brown'), ('Gr', 'Gray'), ('W', 'White'), ('S', 'Silver'), ('Go', 'Gold')], max_length=200),
        ),
        migrations.AlterField(
            model_name='shade',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shade',
            name='second_color',
            field=models.CharField(blank=True, choices=[('P', 'Pinc'), ('Co', 'Corall'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('C', 'Cyan'), ('V', 'Violet'), ('B', 'Black'), ('Br', 'Brown'), ('Gr', 'Gray'), ('W', 'White'), ('S', 'Silver'), ('Go', 'Gold')], max_length=200),
        ),
    ]
