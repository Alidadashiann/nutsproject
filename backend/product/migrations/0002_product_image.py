# Generated by Django 4.2.2 on 2023-06-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product/'),
            preserve_default=False,
        ),
    ]
