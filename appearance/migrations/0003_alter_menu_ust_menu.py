# Generated by Django 4.1 on 2022-09-05 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0002_alter_menu_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ust_menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appearance.menu', verbose_name='üst kategori'),
        ),
    ]
