import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import load_config
from handlers.user import user_router
from keyboards.set_menu import (
    set_main_menu_for_private,
    set_main_menu_for_group
)


logger = logging.getLogger(__name__)


async def main():
    config = load_config()
    logging.basicConfig(
        level=config.log.level,
        format=config.log.format
    )
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Создаем кнопки меню в разных чатах.
    await set_main_menu_for_private(bot)
    await set_main_menu_for_group(bot)

    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
