# Generated by Django 3.2.9 on 2021-12-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211211_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.URLField(default='www.jj.ru'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
