# Generated by Django 3.2.7 on 2021-10-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='телефон'),
        ),
    ]
