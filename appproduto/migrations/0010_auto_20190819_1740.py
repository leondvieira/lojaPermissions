# Generated by Django 2.2.4 on 2019-08-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproduto', '0009_auto_20190819_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='produtos'),
        ),
    ]