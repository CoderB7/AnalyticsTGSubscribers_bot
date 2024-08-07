from django.db import models
from django.utils.translation import gettext as _


class BotUser(models.Model):
    """ Users in chat-bot """
    telegram_id = models.PositiveBigIntegerField(_('ID telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    first_name = models.CharField(_('Name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('Surname'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = 'User of the Bot'
        verbose_name_plural = 'Users of the Bot'


class TelegramChannel(models.Model):  # or TelegramChat
    """Telegram Channel or Group"""
    # bot_user = models.ForeignKey(BotUser, verbose_name=_('User of the Bot'), on_delete=models.CASCADE)
    name = models.CharField(_('Name of the Channel'), max_length=150, blank=True, null=True)
    chat_id = models.BigIntegerField(_('Channel ID'), null=True)
    username = models.CharField(_('Username of the Channel'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Telegram Channel'
        verbose_name_plural = 'Telegram Channels'


class InviteLink(models.Model):
    """An Invitation Link"""
    telegram_channel = models.ForeignKey(TelegramChannel, verbose_name=_('Telegram channel'), on_delete=models.CASCADE)
    creates_join_request = models.BooleanField(_('Request for joining'), default=False)
    name = models.CharField(_('name'), max_length=150, blank=True, null=True)
    link = models.CharField(_('Link'), max_length=150, blank=True, null=True)
    is_revoked = models.BooleanField(_('Is revoked'), blank=True, null=True)
    is_primary = models.BooleanField(_('is_primary'), blank=True, null=True)
    creator = models.CharField(_('creator'), max_length=150, blank=True, null=True)
    expire_date = models.CharField(_('expire_date'), max_length=150, blank=True, null=True)
    member_limit = models.CharField(_('member_limit'), max_length=150, blank=True, null=True)
    pending_join_request_count = models.CharField(_('pending_join_request_count'), max_length=150, blank=True, null=True)
    public_link = models.BooleanField(_('Public link'), default=False)

    def __str__(self):
        return f'{self.link}'

    class Meta:
        verbose_name = 'Invitation link'
        verbose_name_plural = 'Invitation links'


class TelegramSubscriber(models.Model):
    """Telegram Channel users"""
    invite_link = models.ForeignKey(TelegramChannel, verbose_name=_('Invitation Link'), on_delete=models.CASCADE)

    telegram_id = models.PositiveBigIntegerField(_('ID telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=150, blank=True, null=True)
    first_name = models.CharField(_('Name'), max_length=150, blank=True, null=True)
    last_name = models.CharField(_('Surname'), max_length=150, blank=True, null=True)
    subscribed = models.BooleanField(_('Subscribed'), default=False)
    datetime_subscribe = models.DateTimeField(_('Subscription time'), blank=True, null=True)
    datetime_unsubscribe = models.DateTimeField(_('Unsubscription time'), blank=True, null=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

