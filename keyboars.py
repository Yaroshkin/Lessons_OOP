from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup





class Keyboard():
    def __init__(self):
        self.keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    def add_button(self, text: str, callback_data: str=None, url: str=None):
        if url:
            button = InlineKeyboardButton(text=text,url=url)
        elif callback_data:
            button = InlineKeyboardButton(text=text, callback_data=callback_data)
        else:
            raise ValueError('Необходимо указать url или calback_data')
        self.keyboard.inline_keyboard.append([button])

    def get_keyboard(self):
        return self.keyboard
