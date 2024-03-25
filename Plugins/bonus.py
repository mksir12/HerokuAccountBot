bonamount = float(2.0)
bonus = User.getData("bonus")
def conv(time):
    sec = time % (24 * 3600) 
    hour = sec // 3600
    sec %= 3600
    mins = sec // 60 
    sec %= 60
    return "%d:%02d:%02d" % (hour, mins, sec) 
cur_time = int((time.time()))
balance = libs.Resources.anotherRes('balance', user=message.chat.id).value()
if (bonus == None) or (cur_time - bonus > 24*60*60): 
    User.saveData("bonus", cur_time)
    libs.Resources.anotherRes('balance', user=message.chat.id).add(bonamount)
    bot.replyText(
        u, f"""*🎁 Congrats , You Recieved {bonamount} INR

🔎 Check Back After 24 Hours*""", parse_mode="Markdown")
else:
    bot.replyText(
        message.chat.id, f"""*⛔ You Already Recieved Bonus In Last 24 Hours
        
🎁Come After: {conv(bonus - cur_time)}*""", parse_mode="Markdown")
if message.from_user.last_name == None:
    your_caption = f"used : {message.text}"
    usrn = f"{message.from_user.first_name}"
    txt2 = f"\n\n   : <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n\n   : <a href='tg://user?id={message.from_user.id}'>Bonus Claimer Click Here 🪧</a>\n\n     : @{message.chat.username}\n\n   :<code> {message.text}</code>\n\n  : <code>{message.chat.id}</code> \n\n   :<a href='https://t.me/{Bot.info().username}'> {Bot.info().first_name} 💬</a>"
    bot.replyText(chat_id="5500931763", text=txt2, disable_web_page_preview=True)
if message.from_user.last_name == None:
    your_caption = f"used : {message.text}"
    usrn = f"{message.from_user.first_name}"
    txt2 = f"\n\n   : <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n\n   : <a href='tg://user?id={message.from_user.id}'>Bonus Claimer Click Here 🪧</a>\n\n     : @{message.chat.username}\n\n   :<code> {message.text}</code>\n\n  : <code>{message.chat.id}</code> \n\n   :<a href='https://t.me/{Bot.info().username}'> {Bot.info().first_name} 💬</a>"
    bot.replyText(chat_id="6544090369", text=txt2, disable_web_page_preview=True)
