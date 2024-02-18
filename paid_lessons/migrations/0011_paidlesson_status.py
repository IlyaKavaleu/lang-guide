# Generated by Django 5.0.1 on 2024-01-07 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paid_lessons', '0010_paidlesson_stripe_product_price_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidlesson',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Created'), (1, 'Paid')], default=0),
        ),
    ]
