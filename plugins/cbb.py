#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Luffy</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/POCKET_PFM'>PFM</a>\n○ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/PocketFmDailyCH1'>PFM</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='PocketFmDailyCH1'>PFM DAILY</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/weebzonex'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ISSUES', url='https://t.me/PFM_SUPPORT_BOT')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
