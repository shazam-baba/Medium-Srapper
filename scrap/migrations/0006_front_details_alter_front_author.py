# Generated by Django 4.0.3 on 2022-04-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0005_front_text_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='front',
            name='details',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='front',
            name='author',
            field=models.CharField(max_length=2000),
        ),
    ]
