# Generated by Django 5.0.6 on 2024-06-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='autos'),
        ),
    ]
