# Generated by Django 4.1 on 2022-10-13 17:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_projectpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='içerik',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
