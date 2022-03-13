from config.data import ADMINS
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

from agro.models import ZontImages, Zonts
from keyboards.reply_buttons import location_button
from keyboards.inline_button import answer_admin_button, answer_callback
from db.commands import get_user, get_zont_by_id, get_zont_by_user

@dp.message_handler(text="🗺 Sputnik zontlash", state="*")
async def analis_with_sky(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Aynan zontlash zarur bo'lgan joy joylashuvini yuboring.", reply_markup=location_button)

    await state.set_state("get_zont_location")



@dp.message_handler(state="get_zont_location", content_types=types.ContentTypes.LOCATION)
async def get_zont_loc_fun(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    URL = f"http://maps.google.com/maps?q={lat},{lon}"
    user = await get_user(message.from_user.id)

    exist_zont = await get_zont_by_user(user)
    if exist_zont:
        for zont_image in exist_zont:
            try:
                await message.answer_photo(photo=zont_image)
            except:
                pass
        return
        
    else:
        zont = Zonts()
        zont.user = user
        zont.location = URL
        zont.save()

        markup = await answer_admin_button(zont.id)
        await bot.send_message(text=URL, chat_id=ADMINS[0], reply_markup=markup)
    await state.finish()
    await message.answer("Tez orada siz uchun zont maydon tayyorlanadi.")



@dp.callback_query_handler(answer_callback.filter())
async def answer_zont_link(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await call.message.delete()

    zont__id = callback_data.get("zont_id")

    zont = await get_zont_by_id(zont__id)

    await state.update_data(zont__id=zont__id, user_id=zont.user.user_id)
    await call.message.answer("Foydalanuvchi uchun maxsus id yozing...")

    await state.set_state("zont_answer_id")


@dp.message_handler(state="zont_answer_id")
async def get_zont_id(message: types.Message, state: FSMContext):
    zont_id = message.text
    await state.update_data(zont_id=zont_id)

    await message.answer("Foydalanuchi uchun zont rasimlarni yuklang....")

    await state.set_state("zont_answer")



@dp.message_handler(state="zont_answer", content_types=types.ContentType.PHOTO)
async def album_handler(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    user_id = data.get("user_id")
    zont__id = data.get("zont__id")
    zont_id = data.get("zont_id")
    zont = await get_zont_by_id(zont__id)
    
    zont.zont_id = zont_id
    zont.save()
    try:
       
        await bot.send_photo(chat_id=user_id, photo=photo)

        zont_images = ZontImages()
        zont_images.images = photo
        zont_images.zont_id = zont_id
        zont_images.save()
        await state.finish()
        await bot.send_message(chat_id=ADMINS[0], text="Habar yubporildi")
    except Exception as er:
        print(er)


    

