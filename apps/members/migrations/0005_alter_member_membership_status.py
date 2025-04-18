# Generated by Django 5.1.6 on 2025-03-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Suspended', 'Suspended'), ('Declined', 'Declined')], default='Pending', max_length=255),
        ),
    ]
