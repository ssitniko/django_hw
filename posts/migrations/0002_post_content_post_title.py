# Generated by Django 5.1.4 on 2024-12-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=0, max_length=56),
            preserve_default=False,
        ),
    ]