# Generated by Django 4.0.4 on 2022-06-09 14:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
