# Generated by Django 3.2.3 on 2021-05-20 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210516_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-id',)},
        ),
    ]