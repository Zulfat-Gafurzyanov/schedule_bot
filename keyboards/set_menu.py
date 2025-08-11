import os

from aiogram import Bot
from aiogram.types import (
    BotCommand,
    BotCommandScopeChat,
    BotCommandScopeAllPrivateChats
)
from environs import Env

from lexicon.lexicon import COMMANDS_PRIVATE, COMMANDS_GROUP

env = Env()
env.read_env()


async def set_main_menu_for_private(bot: Bot):
    """Функция для настройки кнопки Menu бота в личном чате."""
    commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS_PRIVATE.items()
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats()
        )


async def set_main_menu_for_group(bot: Bot):
    """Функция для настройки кнопки Menu бота в групповом чате."""
    group_chat_id = env('GROUP_CHAT_ID')
    commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS_GROUP.items()
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeChat(chat_id=group_chat_id)
        )
