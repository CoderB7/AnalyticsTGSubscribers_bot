import telebot
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
import logging


bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')
telebot.logger.setLevel(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


@bot.chat_member_handler()
async def chat_member_handler_bot(message):
    status = message.difference.get('status')
    invite_link = message.invite_link
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    invite_link_name = None
    invite_link_url = None
    try:
        invite_link_name = getattr(invite_link, 'name')
        invite_link_url = getattr(invite_link, 'invite_link')
    except AttributeError as err:
        logger.info(f'Did not receive an invite link {err}')
    current_subscriber_status = status[1]
    if current_subscriber_status == 'member':
        status_text = '🚀 Subscribed'
    elif current_subscriber_status == 'left':
        status_text = '🙁 Unsubscribed'
    else:
        status_text = '😱 Unknown'
    text_message = (f'Status: {status_text}\n'
                    f'Name: {full_name}\n'
                    f'ID: {user_id}')
    if username:
        text_message += f'\n<b>Username</b> : @{username}'
    if invite_link_name:
        text_message += f'\nName of the Link: {invite_link_name}'
    if invite_link_url:
        text_message += f'\n<b>URL</b>: {invite_link_url}'
    # logger.info(f'{status=}')
    # logger.info(f'{invite_link_name=}')
    # logger.info(f'{invite_link_url=}')
    # logger.info(f'{full_name=}')
    # logger.info(f'{username=}')
    # logger.info(f'{user_id=}')
    await bot.send_message(chat_id=settings.TELEGRAM_ID_ADMIN, text=text_message)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hello friend'
    await bot.send_message(message.chat.id, text)
    await bot.send_message(message.chat.id, message.chat.id)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)






