import asyncio
import logging
import sys
from config import ADMIN, BOT_TOKEN
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand
from aiogram.utils.markdown import hbold, link
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scraper import scrap
from scrap_redit import scrap as scrap_reddit


dp = Dispatcher()

scheduler = AsyncIOScheduler()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command('find_news'))
async def command_find_handler(message: Message) -> None:
    answer = scrap()
    if answer is not None:
        for i in answer:
            await message.answer(f'{i}: {answer[i]}')
    else:
        await message.answer('нет новостей')


async def start_scrap_bank(bot: Bot):
    answer = scrap()
    if answer is not None:
        for i in answer:
            news_link = f'{i}: {answer[i]}'
            await bot.send_message(ADMIN, news_link)


@dp.message(Command('find_codes'))
async def command_find_handler(message: Message) -> None:
    answer = scrap_reddit()
    if answer is not None:
        for i in answer:
            news_link = f'{i}: {i}'
            await message.answer(news_link)
    else:
        await message.answer('нет новостей')


async def start_scrap_reddit(bot: Bot):
    answer = scrap_reddit()
    if answer is not None:
        for i in answer:
            news_link = f'{i}: {i}'
            await bot.send_message(ADMIN, news_link)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/find_news", description="Искать комбо дни"),
        BotCommand(command="/find_codes", description="Искать коды"),
    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await bot.send_message(ADMIN, "Bot Started")

    await set_commands(bot)

    scheduler.add_job(start_scrap_bank, 'cron', hour=8, minute=00, kwargs={'bot': bot})
    scheduler.add_job(start_scrap_reddit, 'cron', hour=8, minute=00, kwargs={'bot': bot})
    scheduler.add_job(start_scrap_bank, 'cron', hour=18, minute=00, kwargs={'bot': bot})
    scheduler.add_job(start_scrap_reddit, 'cron', hour=18, minute=00, kwargs={'bot': bot})
    scheduler.start()

    # And the run events dispatching
    await dp.start_polling(bot)

# Start the bot
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
