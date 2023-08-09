from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

partners_k: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='SILK WAY RALLY',
                              url='https://silkwayrally.com/')]
    ]
)

our_links: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='SWHL',
                              url='https://swhl.ru/')],
        [
            InlineKeyboardButton(text='Наш ВК',
                                 url='https://vk.com/hockey_rthl'),
            InlineKeyboardButton(text='Наш YouTube-канал',
                                 url='https://www.youtube.com/c/RTHLTV'),
            InlineKeyboardButton(text='Наш Telegram-канал',
                                 url='https://t.me/swhleague')
        ]
    ]
)
