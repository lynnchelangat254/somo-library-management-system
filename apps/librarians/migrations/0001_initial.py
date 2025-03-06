# Generated by Django 5.1.6 on 2025-02-24 13:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_id', models.IntegerField(unique=True)),
                ('date_hired', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Librarian',
                'verbose_name_plural': 'Librarians',
            },
        ),
    ]
