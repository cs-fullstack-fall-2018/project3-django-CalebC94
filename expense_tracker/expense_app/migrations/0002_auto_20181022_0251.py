# Generated by Django 2.0.6 on 2018-10-22 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='balance',
            new_name='balanceHistory',
        ),
    ]
