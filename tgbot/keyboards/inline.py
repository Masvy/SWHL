from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

partners_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='SILK WAY RALLY',
                              url='https://silkwayrally.com/')]
    ]
)

our_links_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сайт SWHL',
                              url='https://swhl.ru/')],
        [
            InlineKeyboardButton(text='ВК',
                                 url='https://vk.com/hockey_rthl'),
            InlineKeyboardButton(text='YouTube',
                                 url='https://www.youtube.com/c/RTHLTV'),
            InlineKeyboardButton(text='Telegram',
                                 url='https://t.me/swhleague')
        ]
    ]
)


stickers_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='SWHL',
                              url='https://t.me/addstickers/swhlStickers')]
    ]
)

players_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅',
                                 callback_data='right'),
            InlineKeyboardButton(text='❌',
                                 callback_data='wrong')
        ]
    ]
)

commands_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅',
                                 callback_data='right_1'),
            InlineKeyboardButton(text='❌',
                                 callback_data='wrong_1')
        ]
    ]
)

statistics_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='СНАЙПЕРЫ',
                                 callback_data='sniper_pressed'),
            InlineKeyboardButton(text='АССИСТЕНТЫ',
                                 callback_data='assists_pressed')
        ],
        [
            InlineKeyboardButton(text='МОМБАРДИРЫ',
                                 callback_data='goalpas_pressed'),
            InlineKeyboardButton(text='ШТРАФЫ',
                                 callback_data='penalties_pressed')
        ],
        [
            InlineKeyboardButton(text='ЛУЧШИЕ',
                                 callback_data='best_pressed'),
            InlineKeyboardButton(text='ВРАТАРИ',
                                 callback_data='goalkeepers_pressed')
        ],
        [
            InlineKeyboardButton(text='СБОРНАЯ',
                                 callback_data='saltworts_pressed'),
            InlineKeyboardButton(text='КОМАНДЫ',
                                 callback_data='teams_pressed')
        ]
    ]
)

admin_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Просмотреть новых игроков',
                              callback_data='view_players')],
        [InlineKeyboardButton(text='Просмотреть новые команды',
                              callback_data='views_commands')]
    ]
)
