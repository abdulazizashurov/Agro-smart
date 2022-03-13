from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


answer_callback = CallbackData("zont", "zont_id")
answer_question_callback = CallbackData("question", "question_id")



async def answer_admin_button(zont_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Javob berish",
                                     callback_data=answer_callback.new(zont_id=zont_id))
            ]
        ]
    )

    return markup



async def answer_question_button(question_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Javob berish",
                                     callback_data=answer_question_callback.new(question_id=question_id))
            ]
        ]
    )
    
    return markup




question_or_photo_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Text", callback_data="question_only"),
            InlineKeyboardButton(text="📸 Rasm + Text", callback_data="question_photo"),
        ],
    ]
)



async def google_data(link):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ushbu muammolar bo'yicha maqolalar", url=link)
            ]
        ]
    )

    return markup