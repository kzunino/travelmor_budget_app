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
            name='Currency',
            fields=[
                ('currency_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=uuid.uuid4, serialize=False)),
                ('currency', models.CharField(max_length=3)),
                ('exchange_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
