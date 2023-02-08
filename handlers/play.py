import random

from aiogram.types import Message

import game
from loader import dp


@dp.message_handler(commands=['play'])
async def mes_play(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!'
                                 '\nЕсли хочешь поменять количество конфет '
                                 '\nВведи команду например - "/play 500".')
            game.total.remove(duel)
            return False
        return True
    else:
        if len(message.text) != 5 and message.text[5:].replace(' ', '').isdigit():
            user_total = int(message.text[5:].replace(' ', ''))
            if user_total > 300:
                await message.answer(f'Привет, {message.from_user.full_name}! '
                                     f'\nНа столе лежит {user_total} конфет(ы)'
                                     f'\nМы будем играть в конфеты. Бери от 1 до 28...')
                my_game = [message.from_user.id, message.from_user.first_name, user_total]
                game.total.append(my_game)
            else:
                await message.answer(f'Какой смысл менять шило на мыло? Вводи больше чем 300!!!')

        else:
            candies_total = random.randint(150, 300)
            await message.answer(f'Привет, {message.from_user.full_name}! '
                                 f'\nНа столе лежит {candies_total} конфет(ы)'
                                 f'\nМы будем играть в конфеты. Бери от 1 до 28...')
            my_game = [message.from_user.id, message.from_user.first_name, candies_total]
            game.total.append(my_game)
