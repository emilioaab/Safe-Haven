# Generated by Django 5.0.3 on 2024-04-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0006_remove_hostreq_image_hostreq_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostreq',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='תמונה של הנכס '),
        ),
    ]