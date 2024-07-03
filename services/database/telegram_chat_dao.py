import logging

from asgiref.sync import sync_to_async
from telebot.types import Chat
from bot.models import TelegramChannel

logger = logging.getLogger(__name__)


@sync_to_async
def update_telegram_chat(chat_data: Chat):
    defaults_dict = {
        'name': chat_data.title,
        'username': chat_data.username,
    }
    telegram_chat, create_status = TelegramChannel.objects.update_or_create(chat_id=chat_data.id, defaults=defaults_dict)

    return telegram_chat

