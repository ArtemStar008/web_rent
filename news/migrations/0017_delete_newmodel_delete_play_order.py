# Generated by Django 4.0.4 on 2022-05-15 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_newmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewModel',
        ),
        migrations.DeleteModel(
            name='Play_order',
        ),
    ]
