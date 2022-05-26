#!/bin/python3

# Libs
import json,random
import datetime, time
import asyncio
import os

from telethon import TelegramClient, events

# Variables
config_path = 'bot_config.json'

# Read config
f = open(config_path, 'r')
conf = json.load(f)
f.close()


answer_how=['Нормльно','Хорошо','Отлично']
answer_what=['Сижу','Лежу','С тобой разговариваю','Отдыхаю']


async def bot():
    async with TelegramClient('bot', conf['app_id'], conf['app_hash']) as tgclient:
        await tgclient.start()

        @tgclient.on(events.NewMessage())
        async def handler(event):
            sender = await event.get_sender()
            sender_dict = sender.to_dict()
            if sender_dict.get('username') != 'rabchik_engineer':
                if event.message.message.find('как дела')!=-1 or event.message.message.find('Как дела')!=-1:
                    await event.reply(answer_how[random.randint(0,len(answer_how)-1)])
                if event.message.message.find('что делаешь?')!=-1 or event.message.message.find('Что делаешь?')!=-1:
                    await event.reply(answer_what[random.randint(0,len(answer_what)-1)])


        await tgclient.run_until_disconnected()


# User(id=1124695321, is_self=False, contact=False, mutual_contact=False, deleted=False, bot=False, bot_chat_history=False, bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False, support=False, scam=False, apply_min_photo=True, fake=False, access_hash=-1546900081710505395, first_name='Валерий', last_name='Рябченко', username='rabchik_engineer', phone=None, photo=UserProfilePhoto(photo_id=5397880207618193497, dc_id=2, has_video=False, stripped_thumb=None), status=UserStatusRecently(), bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None, lang_code='ru')

asyncio.run(bot())
