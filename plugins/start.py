from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("👤 Bot Developer 👤", url="https://t.me/kasu_bro_bot")],
        [InlineKeyboardButton(
            "👥 Support Group 👥", url="https://t.me/epusthakalayabotsupport")],
        [InlineKeyboardButton(
            "📣 Main Channel 📣",url="https://t.me/epusthakalaya_bots")]
    ])
    thumbnail_url = "https://telegra.ph/file/c27a7b9cf0c3d87d4b65d.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hey<b>{message.from_user.first_name}</b>. I'm 𝐘𝗼𝘂𝘁𝘂𝗯𝗲 𝐃𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝐁𝗼𝘁. \n\n<b>Instructions for use..</b>\n• Hit /start to update me.\n• Hit /help to find out more about how to use me .\n───── ❝ **E PUSTHAKALAYA BOTs™** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
