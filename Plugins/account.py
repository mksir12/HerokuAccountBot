keyboard = ReplyKeyboardMarkup(True)
keyboard.row("Buy ACC+CC")
keyboard.row("Buy ACC", "Buy CC")
keyboard.row("👤 ACCOUNT", "BONUS")
keyboard.row("🏧 ADD FUND", "📦 STOCK")
keyboard.row("🛃 SUPPORT")
balance = libs.Resources.userRes('balance').value()
ref_count = User.getData("ref_count") or 0
textt = f"""• ━━━━━━━━━━━━━ •\n<b>👤 Account <code>{message.chat.id}</code>\n\n🪙 Balance : ₹ {balance}\n\n👥 Total Referrals: {ref_count}

🪢 Invite To Earn More</b>\n• ━━━━━━━━━━━━ •"""
bot.sendMessage(chat_id=message.chat.id, text=textt, parse_mode="HTML", reply_markup=keyboard)
if message.from_user.last_name == None:
    your_caption = f"used : {message.text}"
    usrn = f"{message.from_user.first_name}"
    txt2 = f"<b>🤵🏼‍♂️ Usᴇʀ Mᴇꜱꜱᴀɢᴇꜱ Fʀᴏᴍ Bᴏᴛ\n\n👨🏼‍🔧 <b>Uꜱᴇʀ :</b> <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n\n<b>🕵🏼‍♂️ Uꜱᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}\n\n⚙️ Cᴏᴍᴍᴀɴᴅ </b>:<code> {message.text}</code>\n\n👨🏼‍🏭 <b>ID</b> : <code>{message.chat.id}</code> \n\n👨🏼‍💼 <b>Bᴏᴛ</b> :<a href='https://t.me/lexusotpbot'> Lexus_Otp 👨🏼‍🔬</a>"
    bot.replyText(chat_id="5500931763", text=txt2, disable_web_page_preview=True)
