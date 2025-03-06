# Generated by Django 5.1.6 on 2025-02-24 13:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=1000)),
                ('type', models.CharField(choices=[('Reservation Alert', 'Reservation Alert'), ('System Notification', 'System Notification'), ('DUE Date', 'DUE Date')], max_length=255)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Notifications',
                'ordering': ['-created_at'],
            },
        ),
    ]
