# Generated by Django 5.0.7 on 2024-08-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_tourplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='location',
            field=models.CharField(default='s', max_length=255),
            preserve_default=False,
        ),
    ]
