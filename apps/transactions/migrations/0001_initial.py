# Generated by Django 5.1.6 on 2025-02-24 13:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('fine_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('status', models.CharField(choices=[('Borrowed', 'Borrowed'), ('Returned', 'Returned'), ('Overdue', 'Overdue'), ('LOST', 'LOST')], default='Borrowed', max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_transaction', to='books.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_transaction', to='members.member')),
            ],
            options={
                'verbose_name_plural': 'Transaction',
                'ordering': ['-borrow_date'],
            },
        ),
    ]
