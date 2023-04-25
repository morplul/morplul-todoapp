# Generated by Django 4.0.6 on 2023-04-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/default.png', null=True, upload_to='static/users/img/avatars/'),
        ),
    ]