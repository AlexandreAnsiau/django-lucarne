# Generated by Django 4.2.9 on 2024-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='default/profile_images/user.png', null=True, upload_to='profile_images/', verbose_name='photo de profil'),
        ),
    ]