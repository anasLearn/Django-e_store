# Generated by Django 3.2 on 2021-05-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password1',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password2',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
