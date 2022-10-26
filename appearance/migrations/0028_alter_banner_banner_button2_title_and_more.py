# Generated by Django 4.1 on 2022-09-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0027_banner_alter_feature_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_button2_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_button2_url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_button_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_button_url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(help_text='1770x550 boyutunda resim önerilmektedir.', upload_to='media/images/site/banner', verbose_name='Banner resmi'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_order',
            field=models.IntegerField(default=1, verbose_name='Sıra'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_status',
            field=models.CharField(choices=[('Published', 'Yayınla'), ('Draft', 'Taslak')], max_length=100, verbose_name='Banner Statüsü'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
