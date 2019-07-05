from pyrogram import Filters, Message, Emoji, InlineKeyboardMarkup, InlineKeyboardButton

from ..pyrotemplate import PyroTemplate


@PyroTemplate.on_message(Filters.command("start") & Filters.private)
async def start_private(bot: PyroTemplate, msg: Message):
    await msg.reply_text(
        f"Hello {msg.from_user.first_name} {Emoji.WAVING_HAND}"
    )


@PyroTemplate.on_message(Filters.command("help") & Filters.private)
async def help_private(bot: PyroTemplate, msg: Message):
    await msg.reply_text(
        "I'm the [Template](https://github.com/ColinTheShark/Pyrogram-"
        "Template) for a Telegram Bot built with @Pyrogram."
    )
