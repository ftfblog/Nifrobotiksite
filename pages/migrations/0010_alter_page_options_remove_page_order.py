# Generated by Django 4.1 on 2022-10-19 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_page_alter_projectpage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Projeler', 'verbose_name_plural': 'Projeler'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='order',
        ),
    ]
