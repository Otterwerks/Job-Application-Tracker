# Generated by Django 2.2 on 2019-04-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applied_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='closes_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='company_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='user/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='portal_login',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='portal_pass',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='portal_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='posted_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='posting_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='user/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
