# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Country-Info-Bot/blob/main/LICENSE

import os
import pyrogram
import asyncio
import time
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Country Info Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {}, I am a country information finder bot. Give me a country name I will send the informations of the country.

Made by @FayasNoushad
"""
HELP_TEXT = """
- Just send me a country name
- Then I will check and send you the informations

<b><u>Informations :-</u></b>
Name, Native Name, Capital, Population, Region, Sub Region, Top Level Domains, Calling Codes, Currencies, Residence, Timezone, Wikipedia, Google

Made by @FayasNoushad
"""
ABOUT_TEXT = """
- **Bot :** `Country Info Bot`
- **Creator :** [Fayas](https://telegram.me/TheFayas)
- **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Country-Info-Bot/tree/main)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()
        
@Bot.on_message(filters.private & filters.command(["corona"]))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation
    )


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>CURRENT SITUATION</b>' + '\n' + '\n' + '<b>' +
                    update_date_time + ' now </b>' + '\n' + '\n' +
                    '<b>🇱🇰 Situation in Sri Lanka</b>' + '\n' + '\n'  +
                    '🤒 Number of confirmed patients (cumulative) = ' + '<code>' +
                    local_total_cases + '</code>' + '\n' +
                    '🤕 Number of patients receiving treatment = ' + '<code>' + local_active_cases + '</code>' +
                    '\n' + '😷 Number of new patients = ' + '<code>' + local_new_cases + '</code>' +
                    '\n' +
                    '🏥 Persons currently under investigation in hospitals = ' + '<code>' +
                    local_total_number_of_individuals_in_hospitals +  '</code>' + '\n' +
                    '🙂 The number of people who have recovered and left = ' + '<code>' + local_recovered + '</code>' + 
                    '\n' + '⚰ Number of deaths = ' + '<code>'  + local_deaths + '</code>' + '\n' +
                    '\n' + '<b>🌎 Worldwide status</b>' + '\n' +
                    '\n' + '🤒 Number of confirmed patients (cumulative) = ' '<code>'  +
                    global_total_cases + '</code>' + '\n' + '😷 Number of new patients = ' '<code>'  +
                    global_new_cases + '</code>' + '\n' + '⚰ Number of deaths = ' '<code>'  +
                    global_deaths + '</code>' + '\n' + '🙂 Healed number = ' '<code>'  +
                    global_recovered + '</code>' + '\n' + '\n' + '\n' +
                    '✅ All information is provided by the government and reputable sources' + '\n' +
                    '~ @sl_bot_zone 🇱🇰 ~')
    return textt

@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/corona {variabla}'))
async def corona(event):
    await event.respond(sta(),parse_mode='MARKDOWN')
    raise events.StopPropagation

Bot.run()
