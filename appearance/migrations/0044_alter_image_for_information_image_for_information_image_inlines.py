# Generated by Django 4.1 on 2022-09-25 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0043_alter_image_for_information_image_for_information_foregeinkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_for_information',
            name='image_for_information_image_inlines',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appearance.information_gallery'),
        ),
    ]
