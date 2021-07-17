from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("🤖 Other Bots 🤖", url="https://t.me/epusthakalaya_bots/7")],
		 ])
	help_image = "https://telegra.ph/file/bf093f4f785d57665fe16.jpg"
	await message.reply_photo(help_image,  caption="**🆘 Help Menu 🆘**\n• Just Send your Youtube video url \n• And I will give Method list to select your choice. \n\ \n\nJoin @epusthakalaya_bots",reply_markup=Lasiya2)
