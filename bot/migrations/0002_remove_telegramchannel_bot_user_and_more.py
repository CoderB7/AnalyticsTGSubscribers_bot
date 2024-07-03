# Generated by Django 5.0.6 on 2024-07-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramchannel',
            name='bot_user',
        ),
        migrations.AddField(
            model_name='telegramchannel',
            name='chat_id',
            field=models.BigIntegerField(null=True, verbose_name='Channel ID'),
        ),
        migrations.AddField(
            model_name='telegramchannel',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Username of the Channel'),
        ),
    ]
