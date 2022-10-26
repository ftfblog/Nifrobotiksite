# Generated by Django 4.1 on 2022-09-05 17:33

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0005_alter_menu_ust_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='level',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='rght',
            field=models.PositiveIntegerField(default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=3, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='ust_menu',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='appearance.menu', verbose_name='üst kategori'),
        ),
    ]
