# Generated by Django 3.0.3 on 2020-09-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='account_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
