# Generated by Django 5.1.5 on 2025-01-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparkapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
