# Generated by Django 2.2 on 2019-05-13 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20190508_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='last_updated',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
