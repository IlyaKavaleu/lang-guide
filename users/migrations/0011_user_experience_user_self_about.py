# Generated by Django 5.0.1 on 2024-01-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_linkedin_alter_user_family_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='self_about',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
