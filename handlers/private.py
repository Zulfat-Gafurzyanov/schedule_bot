from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from filters.filters import IsOurMember
from lexicon.lexicon import LEXICON


private_router = Router()


@private_router.message(CommandStart(), IsOurMember())
async def start_command(message: Message):
    await message.answer(LEXICON[message.text])


@private_router.message(IsOurMember())
async def another_command(message: Message):
    await message.answer(LEXICON['another'])


@private_router.message()
async def warning_command(message: Message):
    await message.answer(LEXICON['warning'])
