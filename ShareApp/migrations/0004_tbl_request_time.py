# Generated by Django 3.2.7 on 2022-01-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShareApp', '0003_tbl_request_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_request',
            name='time',
            field=models.CharField(default='', max_length=30),
        ),
    ]
