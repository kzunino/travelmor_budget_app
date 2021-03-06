# Generated by Django 3.1.2 on 2020-10-16 19:33

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('expense_type', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=3)),
                ('home_currency', models.CharField(blank=True, max_length=3)),
                ('cost_conversion', models.DecimalField(blank=True, decimal_places=3, max_digits=12)),
                ('exchange_rate', models.DecimalField(decimal_places=3, max_digits=12)),
                ('purchase_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
