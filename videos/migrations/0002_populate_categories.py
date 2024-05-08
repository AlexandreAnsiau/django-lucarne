# Generated by Django 4.2.9 on 2024-05-08 20:10

from django.db import connection, migrations


def populate_categories(apps, schema_editor):
    categories = ["cinema", "clips", "arts", "branding"]

    with connection.cursor() as cursor:
        for category in categories:
            cursor.execute(f"INSERT INTO videos_category (name, is_visible) VALUES ('{category}', TRUE)")


class Migration(migrations.Migration):
    atomic = True

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_categories)
    ]
