# Generated by Django 5.1.4 on 2024-12-07 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]