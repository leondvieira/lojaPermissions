# Generated by Django 2.2.4 on 2019-08-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproduto', '0007_notafiscal_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default=2, height_field=100, upload_to='', width_field=100),
            preserve_default=False,
        ),
    ]