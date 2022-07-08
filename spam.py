from pyrogram import filters,Client
from time import sleep
import time
import random

api_id=#Your-api_id
api_hash="#api_hash"

app = Client("SPAMER", api_id=api_id, api_hash=api_hash)

#####################################global#####################################

spam_txt=''
ss = False
################################################################################
os.system("clear")
print(Fore.BLUE)
print('''██████        ██       █████    ██████         ██
█    █      █    █     █   █    █            █    █
█    █     █      █    █   █    █           █      █
██████    █        █   █████    ██████     █        █
█         ██████████   █   █         █     ██████████
█         █        █   █    █        █     █        █
█         █        █   █     █  ██████     █        █''')

print(Fore.GREEN)
print('BOT IS RUNENED!!!')
with app:
    app.send_message('@YourID',f'''**『 Bot Is Runned ✅ 』**''')
    app.send_message('@YourID',f'''**Bot Is Now Runned On Server . You Can Add Bot In your Group . \n\n Version : 1.2.0**''')
    print(Fore.RED)
    print('''〔𝗕𝗼𝘁 𝗜𝗦 𝗢𝗻𝗹𝗶𝗻𝗲〕''')
################################################################################
@app.on_message(filters.command(['setspam'], '') & filters.user([YourID]) , group=1)
def setspam_command(c, m):
    global spam_txt

    if m.reply_to_message:
        spam_txt = m.reply_to_message.text
        app.send_message(m.chat.id, f"**Spam Text Saved (`{spam_txt}`) **")
    else:
        m.reply_text("**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**")

@app.on_message(filters.command(['spamtext'], '') & filters.user([YourID]) , group=1)
def spamtext_command(c, m):
    global spam_txt

    m.reply_text(f"**『 Spam Text Saved |`{spam_txt}`| 』**")

@app.on_message(filters.command(['spam'], '') & filters.group & filters.user([YourID]) , group=2)
def spam_command(c, m):
    global spam_txt , ss
    ss = True
    gcm = app.get_chat_members(m.chat.id)
    for gg in gcm:
        if ss:
            if gg.user.username:
                    sleep(0.0)
                    if not gg.user.is_bot:
                        try:
                            s = app.send_message(m.chat.id, f"**{spam_txt}**")
                            sleep(0.0)
                            app.send_chat_action(m.chat.id, 'typing')
                            pass
                        except Exception as e:
                            app.send(YourID,f'''**Error ❗️\n\nError Name: {e}\n\n Chat Name: {m.chat.title}\n Chat ID: {m.chat.id}**''')
                            ss = False
                            raise

,reply_to_message_id=m.reply_to_message.message_id
@app.on_message(filters.command(['stop'], '') & filters.user([YourID]) , group=3)
def stop_command(c, m):
    global ss

    ss = False
    m.reply_text(f"**『 SPAM STOPED !』**")

@app.on_message(filters.command(['spamer'], '') & filters.group & filters.user([YourID]) , group=4)
def online_test_command(c, m):

    m.reply_text(f"**『 SPAMER IS ONLINE 』\n\n#աա_ʊռɨȶʏ**")


@app.on_message(filters.command(['join'], '') & filters.user([YourID]) , group=5)
def bot_join(c, m):
    chat_link = m.text.split()[1]
    group=(app.get_chat(chat_link))
    app.join_chat(chat_link)
    m.reply_text(f"**『 Bot Is Joined This Chat 』\n\nChat Name 📟: {group.title} \nChat ID : {group.id} \nChat Members : {group.participants_count} **")

@app.on_message(filters.command(['leave'], '') & filters.user([YourID]) , group=6)
def bot_leave(c, m):
    chat_id = m.text.split()[1]
    group=(app.get_chat(chat_id))
    app.leave_chat(chat_id)
    m.reply_text(f"**『 Bot Is Leaved This Chat 』\n\nChat Name 📟: {group.title} \nChat ID : {group.id} \nChat Members : {group.participants_count} **")

app.run()
