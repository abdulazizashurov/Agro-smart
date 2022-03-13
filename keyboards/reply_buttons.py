from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑‍🎓 Ilmiy tavsiya"),
             KeyboardButton(text="🗺 Sputnik zontlash")
             
        ],
        [
            KeyboardButton(text="🔍 Foto analiz"),
            KeyboardButton(text="📂 Mavjud muammolar")
        ]
    ],
    resize_keyboard=True
)



location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Geolokatsiyani jo’natish", request_location=True),
        ],

    ],
    resize_keyboard=True
)
