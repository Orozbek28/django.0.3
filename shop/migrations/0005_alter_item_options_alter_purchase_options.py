# Generated by Django 4.2 on 2023-04-11 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_purchase_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Покупка', 'verbose_name_plural': 'Покупки'},
        ),
    ]
