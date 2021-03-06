# Generated by Django 3.2.9 on 2022-01-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(choices=[('run_crawler', 'Run Crawler')], max_length=255)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
