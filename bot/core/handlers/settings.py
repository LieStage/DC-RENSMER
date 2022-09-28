# (c) @AbirHasan2005

import asyncio
from pyrogram import types, errors
from configs import Config
from bot.core.db.database import db


async def show_settings(m: "types.Message"):
    usr_id = m.chat.id
    user_data = await db.get_user_data(usr_id)
    if not user_data:
        await m.edit("Failed to fetch your data from database!")
        return
    upload_as_doc = user_data.get("upload_as_doc", False)
    caption = user_data.get("caption", None)
    apply_caption = user_data.get("apply_caption", True)
    thumbnail = user_data.get("thumbnail", None)
    buttons_markup = [
        [types.InlineKeyboardButton(f"ᑌᑭᏞᝪᗩᗞ ᗩᔑ ᖴᏆᏞᗴ {'✅' if upload_as_doc else '❌'}",
                                    callback_data="triggerUploadMode")],
        [types.InlineKeyboardButton(f"ᗩᑭᑭᏞᎩ ᑕᗩᑭᎢᏆᝪᑎ {'✅' if apply_caption else '❌'}",
                                    callback_data="triggerApplyCaption")],
        [types.InlineKeyboardButton(f"ᗩᑭᑭᏞᎩ ᗞᗴᖴᗩᑌᏞᎢ ᑕᗩᑭᎢᏆᝪᑎ {'❌' if caption else '✅'}",
                                    callback_data="triggerApplyDefaultCaption")],
        [types.InlineKeyboardButton("ᔑᗴᎢ ᑕᑌᔑᎢᝪᗰ ᑕᗩᑭᎢᏆᝪᑎ",
                                    callback_data="setCustomCaption")],
        [types.InlineKeyboardButton(f"{'ᑕᕼᗩᑎᏀᗴ' if thumbnail else 'ᔑᗴᎢ'} ᎢᕼᑌᗰᗷᑎᗩᏆᏞ",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("ᔑᕼᝪᗯ ᎢᕼᑌᗰᗷᑎᗩᏆᏞ",
                                                          callback_data="showThumbnail")])
    if caption:
        buttons_markup.append([types.InlineKeyboardButton("ᔑᕼᝪᗯ ᑕᗩᑭᎢᏆᝪᑎ",
                                                          callback_data="showCaption")])
    buttons_markup.append([types.InlineKeyboardButton("ᑕᏞᝪᔑᗴ😃",
                                                      callback_data="closeMessage")])

    try:
        await m.edit(
            text="**𝙃𝙄 𝘿𝙐𝙀𝘿 😜 𝘾𝙇𝙄𝘾𝙆 𝙏𝙃𝙀 𝘽𝙀𝙇𝙊𝙒 𝘽𝙐𝙏𝙏𝙊𝙉𝙎⏹ 𝙏𝙊 𝘾𝙊𝙉𝙁𝙄𝙂𝙐𝙍𝙀🪛 𝙔𝙊𝙐𝙍 𝙎𝙀𝙏𝙏𝙄𝙉𝙂𝙎 ⚙\n\n 𝙃𝙚𝙧𝙚 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙨𝙚𝙩𝙪𝙥 𝙮𝙤𝙪𝙧 𝙨𝙚𝙩𝙩𝙞𝙣𝙜𝙨:\n\n 𝙁𝙀𝘼𝙏𝙐𝙍𝙀𝙎 🌟\n𝘿𝙀𝙁𝘼𝙐𝙇𝙏 𝘾𝘼𝙋𝙏𝙄𝙊𝙉📝\n𝘾𝙐𝙎𝙏𝙊𝙈 𝘾𝘼𝙋𝙏𝙄𝙊𝙉✏️\n𝙏𝙃𝙐𝙈𝘽𝙉𝘼𝙄𝙇🏙\n𝙁𝙄𝙇𝙀 📁/ 𝙑𝙄𝘿𝙀𝙊 🎞**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
            parse_mode="Markdown"
        )
    except errors.MessageNotModified: pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.x)
        await show_settings(m)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err)
