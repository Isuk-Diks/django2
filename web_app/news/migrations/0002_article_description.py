# Generated by Django 3.2.9 on 2022-01-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
