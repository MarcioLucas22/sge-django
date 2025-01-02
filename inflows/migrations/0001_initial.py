# Generated by Django 5.1.3 on 2024-11-08 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='products.products')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='suppliers.supplier')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
