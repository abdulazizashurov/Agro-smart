from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π§βπ Ilmiy tavsiya"),
             KeyboardButton(text="πΊ Sputnik zontlash")
             
        ],
        [
            KeyboardButton(text="π Foto analiz"),
            KeyboardButton(text="π Mavjud muammolar")
        ]
    ],
    resize_keyboard=True
)



location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π Geolokatsiyani joβnatish", request_location=True),
        ],

    ],
    resize_keyboard=True
)
