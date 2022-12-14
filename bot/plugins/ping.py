

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start",]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="๐๐, ๐ ๐๐ข ๐๐๐ฃ๐๐ข๐ ๐ฝ๐ค๐ฉ!\n\n"
             "**I can rename media without downloading it!**\n"
             "**Speed depends on your media DC.**\n\n"
             "**Just send me media and reply to it with** /rename **command.**",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("แแดแขแขแแแแ",
                                      callback_data="showSettings")
        ],[types.InlineKeyboardButton("๐แขแแแฐแทแชแขแ๐",url="https://t.me/movie_time_botonly")]])
    )


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="**I can rename media without downloading it!**\n"
             "**Speed depends on your media DC.**\n\n"
             "**Just send me media and reply to it with** /rename **command.**\n\n"
             "**To set custom thumbnail reply to any image with** /set_thumbnail\n\n"
             "**To see custom thumbnail press** /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("แแดแขแขแแแแ",
                                      callback_data="showSettings")],[types.InlineKeyboardButton("๐ฆแแดแฏ๐ฆ",url="https://t.me/fligher")]])
    )
