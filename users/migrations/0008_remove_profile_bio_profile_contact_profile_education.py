# Generated by Django 4.0 on 2023-03-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(choices=[('0', 'Email'), ('1', 'Phone'), ('2', 'None')], default=('2', 'None'), max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('AUT', 'Austria'), ('DEU', 'Germany'), ('NLD', 'Neitherlands')], default=('AUT', 'Austria'), max_length=100),
        ),
    ]
