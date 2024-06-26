# Generated by Django 5.0.4 on 2024-04-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('icon_url', models.URLField()),
            ],
        ),
    ]
