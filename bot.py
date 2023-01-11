from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import uuid
import requests
bot = Bot("5953506929:AAELqHGJICkc-HvDXVbQx7n_-AWFVA3g0mU")
dp = Dispatcher(bot, storage=MemoryStorage())
class Token(StatesGroup):
    token = State()


@dp.message_handler(commands=['start'])
async def get_token(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/token")
    await message.reply("Привет, для начала отправь свой токен с личного кабинета", reply_markup=keyboard)



@dp.message_handler(commands=['token'], content_types=["text"])
async def token(message: types.Message):
    await message.reply("Отправь свой токен", reply_markup=types.ReplyKeyboardRemove())
    await Token.token.set()


@dp.message_handler(state=Token.token)
async def set_token(message:types.Message, state: FSMContext):

    async with state.proxy() as proxy:
        proxy['token'] = message.text
        print(message)
        token = message["text"]
        print(message["text"])
        chat_id = message["chat"]["id"]
        print(chat_id)
        try:
            patch = requests.patch(f"http://85.198.91.34:8000/api/chat-id/{token}/", json={"chat_id": str(chat_id)})
            print(patch.status_code)
            print(patch.content)
            if patch.status_code == 200:

                await message.answer("Я сохранил твой токен")

                await state.finish()

            else:
                await message.answer("Invalid token")
        except:
            await message.answer("token is not valid")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)