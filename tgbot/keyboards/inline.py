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
