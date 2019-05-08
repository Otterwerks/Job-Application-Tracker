# Generated by Django 2.2 on 2019-05-08 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0003_auto_20190508_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(default='Note', max_length=50)),
                ('event_text', models.TextField(blank=True, null=True)),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Application')),
            ],
        ),
    ]
