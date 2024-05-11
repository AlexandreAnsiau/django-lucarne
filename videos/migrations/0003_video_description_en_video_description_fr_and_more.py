# Generated by Django 4.2.9 on 2024-05-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_populate_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='description_fr',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='nom'),
        ),
        migrations.AddField(
            model_name='video',
            name='name_fr',
            field=models.CharField(max_length=500, null=True, verbose_name='nom'),
        ),
    ]
