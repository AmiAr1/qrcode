

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from config import bot
import pyqrcode

# class FSMAdmin(StatesGroup):
#     get_text = State()

#
# async def fsm_qr_start(message: types.Message):
#     if message.chat.type == "private":
#         await FSMAdmin.get_text.set()
#         await bot.send_message(
#             message.chat.id,
#             f"Привет {message.from_user.full_name}, "
#             f"отправь мне любой текст или ссылку\n"
#             f"Для выхода из режима нажми на кнопку /cancel_qr",
#         )
#     else:
#         await message.answer("Пиши в личку!")


async def qrcod(message: types.Message, state: FSMContext):
    qr_code = pyqrcode.create(message.text)
    qr_code.png("media/code.png")
    photo = open("media/code.png", 'rb')
    await bot.send_photo(message.from_user.id, photo,
                         caption="Вот QR код готов")




def register_handler_fsmqrcode(dp: Dispatcher):

    dp.register_message_handler(qrcod,  commands=['qr'])