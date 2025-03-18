# Generated by Django 5.1.6 on 2025-03-18 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_membership_status'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='members.member'),
            preserve_default=False,
        ),
    ]
