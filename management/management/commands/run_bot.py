from django.core.management.base import BaseCommand

from bot.main_bot import bot
import asyncio


class Command(BaseCommand):
    help = "Starting the bot"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
