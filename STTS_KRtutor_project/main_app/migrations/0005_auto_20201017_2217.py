# Generated by Django 3.1.2 on 2020-10-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201017_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapternumberdb',
            name='InnerChapOne',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='chapternumberdb',
            name='InnerChapTwo',
            field=models.IntegerField(default=2),
        ),
    ]
