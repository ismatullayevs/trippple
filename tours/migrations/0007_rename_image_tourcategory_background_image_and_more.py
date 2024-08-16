# Generated by Django 5.0.7 on 2024-08-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_tourcategory_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourcategory',
            old_name='image',
            new_name='background_image',
        ),
        migrations.AddField(
            model_name='tourcategory',
            name='fontawesome_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
