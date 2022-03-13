import time
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from keyboards.inline_button import google_data
from funcs.api import analisImage


@dp.message_handler(text="🔍 Foto analiz", state="*")
async def analis(message: types.Message, state: FSMContext):
    await message.answer("Bizga o'z o'simligingiz rasimini yuboring....")
    await state.set_state("get_illness_photo")



@dp.message_handler(state="get_illness_photo", content_types=types.ContentType.PHOTO)
async def get_images(message: types.Message, state: FSMContext):
    photo_id = await message.photo[-1].download()
    sticker_id = "CAACAgIAAxkBAAIB92Itj61ahxwvlPkw4vpzSYdSMTcGAAKiAQACVp29CkGecjt5EfXdIwQ"
    message_some_id = (await message.answer_sticker(sticker=sticker_id)).message_id

    time.sleep(2)
   
    data = analisImage(str(photo_id).split("'")[1])
    
    if data:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_some_id)
        markup = await google_data(data)
        await message.answer("Hurmatli foydalanuvchi siz uchun biz bir qanchu ma'lumotlani google platformasidan qidirib topdik",
        reply_markup=markup
        )
        await state.finish()
    





