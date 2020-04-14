# Generated by Django 3.0.5 on 2020-04-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rul', '0010_auto_20200414_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shade',
            name='color',
            field=models.CharField(choices=[('P', 'Pink'), ('L', 'Lilac'), ('C', 'Corall'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('Pu', 'Purple'), ('Bk', 'Black'), ('Br', 'Brown'), ('Be', 'Beige'), ('Gr', 'Gray'), ('W', 'White'), ('S', 'Silver'), ('Co', 'Cooper'), ('Go', 'Gold')], max_length=200),
        ),
        migrations.AlterField(
            model_name='shade',
            name='second_color',
            field=models.CharField(blank=True, choices=[('P', 'Pink'), ('L', 'Lilac'), ('C', 'Corall'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('Pu', 'Purple'), ('Bk', 'Black'), ('Br', 'Brown'), ('Be', 'Beige'), ('Gr', 'Gray'), ('W', 'White'), ('S', 'Silver'), ('Co', 'Cooper'), ('Go', 'Gold')], max_length=200),
        ),
    ]
