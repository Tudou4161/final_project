# Generated by Django 3.1.2 on 2020-10-17 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_chapternumberdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapternumberdb',
            old_name='Chap_No',
            new_name='ChapNo',
        ),
        migrations.RenameField(
            model_name='conversationpracticequestiondb',
            old_name='Chap_No',
            new_name='ChapNo',
        ),
        migrations.RenameField(
            model_name='essentialsentencedb',
            old_name='Chap_No',
            new_name='ChapNo',
        ),
    ]