# Generated by Django 4.0.4 on 2022-05-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_rename_orders_play_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitone', models.CharField(max_length=50, verbose_name='Unit_one')),
            ],
            options={
                'verbose_name': 'Заказ_проба',
                'verbose_name_plural': 'Заказ_проба_мн',
            },
        ),
    ]
