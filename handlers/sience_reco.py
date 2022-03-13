
from curses.ascii import FS
import typing
from agro.models import Questions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_media_group import MediaGroupFilter, media_group_handler
from config.data import ADMINS

from keyboards.inline_button import question_or_photo_button, answer_question_callback, answer_question_button
from loader import dp, bot

from db.commands import get_user, get_question




@dp.message_handler(text="🧑‍🎓 Ilmiy tavsiya", state="*")
async def sicence_reco(message: types.Message, state: FSMContext):
    await state.finish()
    text = "O'zingiz uchun qulay bo'lgan yo'l orqali habaringizni yuboring..."
    await message.answer(text=text,reply_markup=question_or_photo_button)

    await state.set_state("sicense_rec")



@dp.callback_query_handler(text="question_photo", state="sicense_rec")
async def get_question_with_photo(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    text = "Hurmatliy user siz eng kamida 2ta eng ko'pi bilan 10 dona rasim yuborishingiz mumkin!"
    await call.message.answer(text)
    await state.update_data(user_id=call.from_user.id)
    await state.set_state("sicense_photo")


@dp.message_handler(MediaGroupFilter(), state="sicense_photo", content_types=types.ContentType.PHOTO)
@media_group_handler
async def album_handler(messages: typing.List[types.Message], state: FSMContext):
    media_group = types.MediaGroup()
    data = await state.get_data()
    user_id = data.get("user_id")
    text = "Juda yaxshi,endi sizni qiziqtirgan savolingizni yozma tarizda yuboring..."
    try:
        images = ""
        for message in messages:
            media_group.attach_photo(f'{message.photo[-1].file_id}', 'media')
            images += f"{message.photo[-1].file_id},"
        await state.update_data(media_group=media_group, images=images)
        await bot.send_message(chat_id=user_id, text=text)
        await state.set_state("sicense_photo_text")

    except Exception as er:
        print(er)


@dp.message_handler(state="sicense_photo_text")
async def get_text_for_photo(message: types.Message, state: FSMContext):
    question_text = message.text
    data = await state.get_data()
    media_group = data.get("media_group")
    images = data.get("images")
    user = await get_user(message.from_user.id)
    text = """
ID: {}
Ism: {} 

"<i>{}</i>"
    """.format(user.user_id, user.name, question_text)
    question = Questions()
    question.question = question_text
    question.images=images
    question.user = user
    question.save()

    markup = await answer_question_button(question.id)
    for admin in ADMINS:
        try:
            await bot.send_media_group(chat_id=admin, media=media_group)
            await bot.send_message(chat_id=admin, text=text, reply_markup=markup)
        except:
            pass
    await message.answer("Habaringiz yuborildi tez orada mutaxasislarimiz sizga o'z javoblarni yuboradilar...")
    await state.finish()



@dp.callback_query_handler(text="question_only", state="sicense_rec")
async def get_question_only_text(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Sizni qiziqtirgan savolingizni yozma tarizda yuboring...")
    await state.update_data(user_id=call.from_user.id)
    await state.set_state("sicense_rec_question")


@dp.message_handler(state="sicense_rec_question")
async def get_text_for_question(message: types.Message, state: FSMContext):
    question_text = message.text
    user = await get_user(message.from_user.id)
    text = """
ID: {}
Ism: {} 

"<i>{}</i>"
    """.format(user.user_id, user.name, question_text)


    question = Questions()
    question.question = question_text
    question.user = user
    question.save()

    markup = await answer_question_button(question.id)
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text=text, reply_markup=markup)
        except:
            pass
    await message.answer("Habaringiz yuborildi tez orada mutaxasislarimiz sizga o'z javoblarni yuboradilar...")
    await state.finish()



@dp.callback_query_handler(answer_question_callback.filter())
async def answer_to_question(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup()
    question_id = callback_data.get("question_id")
    question = await get_question(question_id)
    if question:
        await call.message.answer("Javobingizni yuboring...")
        await state.update_data(question_id=question_id)
        await state.set_state("answer_question")
    


@dp.message_handler(state="answer_question")
async def answer_question_to_user(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    question_id = data.get("question_id")
    question = await get_question(question_id)
    text = f"""
<b>Savol:</b> "<i>{question.question}</i>"

<b>Javob:</b> <i>({text})</i>
"""
    await bot.send_message(chat_id=question.user.user_id, text=text)
    await message.answer("Habaringiz yuborildi")

    await state.finish()

