# Generated by Django 5.1.3 on 2024-11-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwopgg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomreviewdev',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]