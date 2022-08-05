from aiogram.utils import executor
import logging

from aiogram import types

from config import bot, dp
import pyqrcode


@dp.message_handler()
async def echo(message: types.Message):
    qr_code = pyqrcode.create(message.text)
    qr_code.png("media/code.png")
    photo = open("media/code.png", 'rb')
    await bot.send_photo(message.from_user.id, photo,
                         caption="Вот QR код готов")



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)