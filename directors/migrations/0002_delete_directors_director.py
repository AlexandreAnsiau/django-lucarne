# Generated by Django 4.2.9 on 2024-05-08 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
        ('directors', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Directors',
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
            ],
            options={
                'verbose_name': 'réalisateur',
                'verbose_name_plural': 'réalisateurs',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('registrations.customuser',),
        ),
    ]
