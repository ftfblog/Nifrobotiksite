# Generated by Django 4.1 on 2022-09-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0038_remove_image_for_information_image_for_information_foregeinkey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_for_information',
            name='image_for_information_foregeinkey',
            field=models.ManyToManyField(blank=True, null=True, to='appearance.image_for_information', verbose_name='Resim Seçimi'),
        ),
    ]
