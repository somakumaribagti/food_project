# Generated by Django 5.0.6 on 2024-08-04 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0002_alter_book_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='Number',
            field=models.IntegerField(),
        ),
    ]
