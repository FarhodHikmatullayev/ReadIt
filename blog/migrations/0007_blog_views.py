# Generated by Django 4.2.1 on 2023-06-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.ImageField(default=0, editable=False, upload_to=''),
        ),
    ]
