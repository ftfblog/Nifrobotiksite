# Generated by Django 4.1 on 2022-10-25 20:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_page_içerik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='içerik',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
