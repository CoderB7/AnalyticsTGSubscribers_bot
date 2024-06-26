from django.core.management.base import BaseCommand

from bot.main_bot import bot
from django.conf import settings
from telebot import util
import asyncio
import logging


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Starting the bot"

    def handle(self, *args, **options):
        try:
            asyncio.run(bot.infinity_polling(logger_level=settings.LOG_LEVEL, allowed_updates=util.update_types))  # to show errors
        except Exception as err:
            logger.error(f'Error: {err}')

