# Generated by Django 3.1.2 on 2020-11-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programrecord',
            name='now_offline_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='programrecord',
            name='now_online_count',
            field=models.IntegerField(default=0),
        ),
    ]
