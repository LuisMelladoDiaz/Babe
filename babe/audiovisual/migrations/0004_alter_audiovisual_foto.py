# Generated by Django 5.1.4 on 2025-01-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiovisual', '0003_alter_audiovisual_fecha_alter_audiovisual_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiovisual',
            name='foto',
            field=models.ImageField(blank=True, default='audiovisuals/imagen_generica.jpg', null=True, upload_to='audiovisuals/%Y/%m/%d/'),
        ),
    ]
