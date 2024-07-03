import logging

from asgiref.sync import sync_to_async
from telebot.types import Chat
from bot.models import TelegramChannel, InviteLink

logger = logging.getLogger(__name__)


async def update_invite_link(telegram_chat: TelegramChannel, link_data: Chat):
    defaults_dict = {
        'name': chat_data.title,
        'username': chat_data.username,
    }
    telegram_chat, create_status = InviteLink.objects.aupdate_or_create(chat_id=chat_data.id, defaults=defaults_dict)

    return create_status


async def create_public_link(telegram_chat: TelegramChannel):
    try:
        await InviteLink.objects.aget(telegram_chat=telegram_chat, public_link=True)
    except InviteLink.DoesNotExist:
        logger.info(f'Could not find links for the channel {telegram_chat.username}')

        await InviteLink.objects.acreate(telegram_chat=telegram_chat, public_link=True)
        return True
    return False

