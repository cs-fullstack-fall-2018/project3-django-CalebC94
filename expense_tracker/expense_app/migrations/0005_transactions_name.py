# Generated by Django 2.0.6 on 2018-10-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0004_auto_20181024_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
