import json

from aiogram.filters import BaseFilter
from aiogram.types import Message
from environs import Env

env = Env()
env.read_env()


class IsOurMember(BaseFilter):
    """
    Фильтр который проверят, является ли пользователь 'своим'.
    """
    async def __call__(self, message: Message) -> bool:
        member_ids_json = env.str("MEMBER_IDS")
        member_ids: dict[str, str] = json.loads(member_ids_json)
        return str(message.from_user.id) in member_ids
