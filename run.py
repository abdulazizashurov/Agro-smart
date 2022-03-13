from loader import bot, storage
import os
import django

async def on_shutdown(dp):
    await bot.close()
    await storage.close()



def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "agro_api.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)