# Generated by Django 5.1.5 on 2025-01-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkapp', '0006_eventtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
    ]
