# Generated by Django 5.0.6 on 2024-07-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
