# Generated by Django 4.0.3 on 2022-03-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]
