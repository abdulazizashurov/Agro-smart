from aiogram import types
from keyboards.inline_button import answer_question_button
from loader import dp
from aiogram.dispatcher import FSMContext

from db.commands import get_questions


@dp.message_handler(text="📂 Mavjud muammolar", state="*")
async def problem(message: types.Message, state: FSMContext):
    questions = await get_questions()
    
    for quesion in questions:
        desc = quesion.question
        markup = await answer_question_button(quesion.id)
        if quesion.images:
            images = str(quesion.images).split(",")
            print(images)
            for image in images:
                try:
                    await message.answer_photo(photo=image, caption=desc, reply_markup=markup)
                except:
                    pass
        else:
            await message.answer(text=desc, reply_markup=markup)

