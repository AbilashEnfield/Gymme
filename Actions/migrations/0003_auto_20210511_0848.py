# Generated by Django 3.2 on 2021-05-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0002_chatroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='explorevideos',
            name='CommentCount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='explorevideos',
            name='likeCount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='explorevideos',
            name='shareCount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]