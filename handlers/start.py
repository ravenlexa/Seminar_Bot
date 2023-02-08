from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}! '
                         f'Вот мои команды: /start, /play, /help.')
