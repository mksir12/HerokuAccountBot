AllBanUsers = Bot.getData("AllBanUsers")
if AllBanUsers == None:
    AllBanUsers = "12345"
for userid in AllBanUsers:
    if str(userid) == str(message.chat.id):
        bot.replyText(u, "<b><i>🚫You are Banned in this Bot</i></b> ")
        raise ReturnCommand()
if "ACC+CC" in message.text:
    Bot.runCommand("ACC+CC")
elif "ACC" in message.text:
    Bot.runCommand("ACC")
elif "CC" in message.text:
    Bot.runCommand("CC")
elif "/bonus" in message.text:
    Bot.runCommand("BONUS")
elif "help" in message.text:
    Bot.runCommand("/help")
elif "Help" in message.text:
    Bot.runCommand("/help")
elif "FREE" in message.text:
    Bot.runCommand("FREE")   
elif "📦 STOCK" in message.text:
    Bot.runCommand("STOCK")   
elif "👤 ACCOUNT" in message.text:
    Bot.runCommand("/accountt")
    
if message.from_user.last_name == None:
    your_caption = f"used : {message.text}"
    usrn = f"{message.from_user.first_name}"
    txt2 = f"<b>💹 Usᴇʀ Mᴇꜱꜱᴀɢᴇꜱ Fʀᴏᴍ Bᴏᴛ 🔑\n\n🗣️ <b>Uꜱᴇʀ :</b> <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n\n<b>💱 Uꜱᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}\n\n🛂 Cᴏᴍᴍᴀɴᴅ </b>:<code> {message.text}</code>\n\n🔃<b> ID</b> : <code>{message.chat.id}</code> \n\n🦾 <b>Bᴏᴛ</b> :<a href='https://t.me/{Bot.info().username}'> {Bot.info().first_name} 💬</a>"
    bot.replyText(chat_id="5500931763", text=txt2, disable_web_page_preview=True)
