# Generated by Django 5.0.1 on 2024-01-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_opening_speech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='opening_speech',
            field=models.TextField(max_length=2000),
        ),
    ]
