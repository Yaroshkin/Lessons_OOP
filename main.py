import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery
import os
from dotenv import load_dotenv
from models_db import Db
from keyboars import Keyboard



class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.db = Db('my_database.db')
        self.keyboard = Keyboard()

        # Регистрируем обработчики
        self.dp.message.register(self.start_command, Command("start"))
        self.dp.callback_query.register(self.button_handler)

    async def start_command(self, message: types.Message):
        user_id = message.from_user.id
        username = message.from_user.username or "Нет имени"
        self.db.creat_table(name='new')
        self.db.insert_user(user_id, username)
        await message.answer("Привет, нажми на кнопку:", reply_markup=self.get_main_keyboard())

    def get_main_keyboard(self):
        self.keyboard.add_button("Ссылка 1",url="https://t.me/chanmusic12")
        self.keyboard.add_button("Ссылка 2", "btn_2")
        return self.keyboard.get_keyboard()

    async def button_handler(self, callback_query: CallbackQuery):
        callback_data = callback_query.data
        if callback_data == "btn_1":
            await callback_query.message.answer( "https://t.me/vilkedrin")
        elif callback_data == "btn_2":
            await callback_query.message.answer("Вы нажали кнопку 2!")

    async def run(self):
        """Запуск бота"""
        logging.basicConfig(level=logging.INFO)
        await self.dp.start_polling(self.bot)

if __name__ == "__main__":
    load_dotenv()
    bot = TelegramBot(os.getenv('BOT_TOKEN'))
    try:
        asyncio.run(bot.run())  # Запуск через asyncio.run()
    except KeyboardInterrupt:
        print("Exit")
