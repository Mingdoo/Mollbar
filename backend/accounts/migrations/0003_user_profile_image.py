# Generated by Django 3.2.9 on 2021-11-24 16:00

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_image/%Y/%m'),
        ),
    ]
