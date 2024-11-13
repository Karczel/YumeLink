# Generated by Django 5.1.2 on 2024-11-13 06:07

import yumelinkapp.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yumelinkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chat_name',
            field=models.CharField(default='Untitled', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='share_type',
            field=models.CharField(choices=[('link', 'Link'), ('line', 'Line'), ('facebook', 'Facebook'), ('tumblr', 'tumblr')], default=yumelinkapp.utils.ShareType['link'], max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]