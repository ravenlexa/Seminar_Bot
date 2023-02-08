from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    greetings = ('Привет, давай поиграем в игру под названием - "Конфеты"!\n'
                 'Правила игры:\n'
                 'Играют два игрока делая ход друг после друга,\n'
                 'Второй игрок - бот.\n'
                 'За один ход можно забрать не более чем 28 конфет.\n'
                 'По умолчанию разыгрывается от 150 до 300 конфет\n'
                 'Или напишите сколько конфет вы хотите разыграть.\n'
                 'Все конфеты оппонента достаются сделавшему последний ход.\n')
    await message.answer(greetings)
    print(message.from_user.id)
