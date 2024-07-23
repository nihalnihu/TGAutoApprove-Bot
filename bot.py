from flask import Flask
import threading
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, Message, InlineKeyboardButton, InlineKeyboardMarkup
import config
from database import add_user, add_group, all_users, all_groups, users, remove_user

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    return 'Healthy', 200

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    bot = Client("Auto Approve Bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)


    welcome=[ "https://telegra.ph/file/95a87ff98569910c3a50e.mp4", ]

    
@bot.on_chat_join_request()
async def approval(app: Client, m: ChatJoinRequest):
    usr = m.from_user
    cht = m.chat
    
    try:
        
        group_info = await app.get_chat(cht.id)
        group_name = group_info.title
        username = group_info.username if group_info.username else None
        add_group(cht.id, username, group_name)
        
        await app.approve_chat_join_request(cht.id, usr.id)
        gif = random.choice(welcome)
        await app.send_animation(chat_id=usr.id, animation=gif, caption=f"Hey There {usr.first_name}\nWelcome To {cht.title}\n\n{usr.first_name} Your Request To Join {cht.title} Has Been Accepted By {app.me.first_name}")
        add_user(usr.id)
    except (UserIsBlocked, PeerIdInvalid):
        pass
    except Exception as err:
            print(str(err))

@bot.on_message(filters.command("start") & filters.private)
async def start(app: Client, msg: Message):
    if config.FSUB:
        try:
            await app.get_chat_member(chat_id=config.CHANNEL, user_id=msg.from_user.id)
            add_user(msg.from_user.id)
            await msg.reply_photo(
                photo="https://telegra.ph/file/48e5d712212fe8891dd36.jpg",
                caption=f"Hᴇʟʟᴏ {msg.from_user.mention}...😌\n\n  ☉︎ Tʜɪs ɪs {app.me.mention},\n\n➲ A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.\n\n➲ Jᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɡʜᴛs..",
                reply_markup=InlineKeyboardMarkup([
                        [
                            InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name} ᴛᴏ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{app.me.username}?startchannel=true")],
                        [
                            InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name} ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.me.username}?startgroup=true")],
                        [
                            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/TG_BotCreator")]
                    ])
                )
        except UserNotParticipant:
            await msg.reply_text(text=f"ᴛᴏ ᴜsᴇ {app.me.mention}, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴᴇᴅ ɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ!!",
                                 reply_markup=InlineKeyboardMarkup([
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{config.CHANNEL}")],
                        [
                            InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ ✔︎", url=f"https://t.me/{app.me.username}?start=start")]
                    ])
                )
        except ChatAdminRequired:
            await app.send_message(text=f"I'm not admin in fsub chat, Ending fsub...", chat_id=config.OWNER_ID)
        else:
            await msg.reply_photo(
                photo="https://telegra.ph/file/48e5d712212fe8891dd36.jpg",
                caption=f"Hᴇʟʟᴏ {msg.from_user.mention}...😌\n\n  ☉︎ Tʜɪs ɪs {app.me.mention},\n\n➲ A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.\n\n➲ Jᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs/ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs.",
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name}", url=f"https://t.me/{app.me.username}?startchannel=true")],
                    [
                        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/TG_BotCreator")]
                ])
            )
            add_user(msg.from_user.id)

    @bot.on_message(filters.command("stats") & filters.user(config.OWNER_ID))
    async def dbtool(app: Client, m: Message):
        xx = all_users()
        x = all_groups()
        await m.reply_text(text=f"Stats for {app.me.mention}\n🙋‍♂️ Users : {xx}\n👥 Groups : {x}")

    bot.run()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    run_bot()
