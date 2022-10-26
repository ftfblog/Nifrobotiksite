# Generated by Django 4.1 on 2022-09-23 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0032_alter_information_gallery_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information_gallery',
            name='information_gallery_image_inlines',
        ),
        migrations.AddField(
            model_name='image_for_information',
            name='image_for_information_image_inlines',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='appearance.information_gallery'),
            preserve_default=False,
        ),
    ]
