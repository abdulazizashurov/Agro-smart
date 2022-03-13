from loader import dp
from aiogram import types
from keyboards.reply_buttons import menuButton
from aiogram.dispatcher import FSMContext
from db.commands import get_user, add_user


@dp.message_handler(commands=['start'], state="*")
async def do_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = await get_user(message.from_user.id)
    text = "Assalomu alaykum Agro-smartga hush kelibsiz"
    if user:
        await message.answer(text, reply_markup=menuButton)

    else:
        await add_user(message.from_user.id, message.from_user.full_name)
        await message.answer(text, reply_markup=menuButton)