from django.contrib import admin
from bot.models import BotUser, TelegramChannel, TelegramSubscriber, InviteLink
from django.db.models import ManyToOneRel


def get_fields_for_model(db_model) -> list[str]:
    fields = []
    for field in db_model._meta.get_fields():
        if isinstance(field, ManyToOneRel):
            continue
        fields.append(field.name)
    return fields


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(BotUser)
    search_fields = ['telegram_id', 'username', 'first_name', 'last_name']
    list_editable = ['first_name']
    list_filter = ['first_name']


@admin.register(TelegramChannel)
class TelegramChannelAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(TelegramChannel)


@admin.register(InviteLink)
class InviteLinkAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(InviteLink)


@admin.register(TelegramSubscriber)
class TelegramSubscriberAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(TelegramSubscriber)



