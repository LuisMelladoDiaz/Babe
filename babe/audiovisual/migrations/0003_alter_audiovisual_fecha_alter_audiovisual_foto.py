# Generated by Django 5.1.4 on 2025-01-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiovisual', '0002_alter_audiovisual_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiovisual',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiovisual',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='audiovisuals/%Y/%m/%d/'),
        ),
    ]
