from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
import config

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def setup_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/show", description="показать список и рассчёт"),
        BotCommand(command="/add", description="добавить"),
        BotCommand(command="/del", description="удалить")
    ]

    #await bot.set_my_commands(commands)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=setup_bot_commands)

