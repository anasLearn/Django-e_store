# Generated by Django 3.2 on 2021-05-12 16:37

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210512_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password2',
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
