# Generated by Django 4.2 on 2023-04-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
