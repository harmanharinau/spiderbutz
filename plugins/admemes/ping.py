"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "You are not dead. You are still here. You have no love for me now. Okay .. you're not changed like you used to be..🙂" 
HOW_TO_OWN = "<b>ᴡᴀᴛᴄʜ ᴛᴜᴛᴏʀɪᴀʟ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴍᴀᴋᴇ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ ›› https://youtu.be/MfUjmZ1mpfc</b>"
CONTACT = "<b>ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ ᴏʀ ᴀɴʏ ᴅᴏᴜʙᴛ ᴛʜᴇɴ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ</b> ›› https://t.me/cyniteOfficial</b>"
ZSEARCHERBOT = "<b>𝙱𝙾𝚃 ›› https://t.me/zsearcherbot</b>"
HQ_MOVIES = "<b>ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ</b> ›› http://cloudmine.herokuapp.com/%5B4k_1080p_720p_Files:%5D/\n\n<b>( ʀᴇʟᴏᴀᴅ ᴡᴇʙsɪᴛᴇ ɪғ ɴᴏᴛ ᴏᴘᴇɴs ) ›› http://cloudmine.herokuapp.com/%5B4k_1080p_720p_Files:%5D/</b>\n\n<b>ᴜsᴇʀɴᴀᴍᴇ : A ›› ᴘᴀssᴡᴀʀᴅ : B</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("how_to_own", COMMAND_HAND_LER) & f_onw_fliter)
async def how_to_own(_, message):
    await message.reply_text(HOW_TO_OWN)

@Client.on_message(filters.command("hq_movies", COMMAND_HAND_LER) & f_onw_fliter)
async def hq_movies(_, message):
    await message.reply_text(HQ_MOVIES)


@Client.on_message(filters.command("contact", COMMAND_HAND_LER) & f_onw_fliter)
async def contact(_, message):
    await message.reply_text(CONTACT)


@Client.on_message(filters.command("zsearcherbot", COMMAND_HAND_LER) & f_onw_fliter)
async def Zsearcherbot(_, message):
    await message.reply_text(ZSEARCHERBOT)


