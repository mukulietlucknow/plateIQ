# Generated by Django 3.0.3 on 2020-09-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_status_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='digitalized',
            field=models.BooleanField(default=False),
        ),
    ]
