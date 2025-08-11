from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from filters.filters import IsOurMember
from lexicon.lexicon import LEXICON


user_router = Router()


@user_router.message(CommandStart(), IsOurMember())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
