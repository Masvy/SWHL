# import requests
# import pandas as pd
#
# from pretty_html_table import build_table
# import imgkit
#
# import subprocess
#
#
# def SWHL_sniper():
#     url = "https://swhl.ru/tournament/1033299/stats/best-players?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)
#
#     return df_list[0]
#
#
# html_table = build_table(SWHL_sniper(), 'blue_dark', text_align='left', font_size='25px', padding='1px')
#
# con = imgkit.config(wkhtmltoimage='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
# imgkit.from_string(html_table, 'best.png', config=con)
#
# imgkit.from_string(html_table, "best.png")
#
# # картинку при необходимости подрезать
#
# subprocess.Popen( "best.png", shell=True)


# def SWHL_assists():
#     url = "https://swhl.ru/tournament/1033299/stats/assists?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_assists(), 'blue_dark',
#                          text_align='left', font_size='13px', padding='3px')

# imgkit.from_string(html_table, "tgbot/pictures/assists.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/assists.png"])


# def SWHL_goalpas():
#     url = "https://swhl.ru/tournament/1033299/stats/goalpas?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_goalpas(), 'blue_dark',
#                          text_align='left', font_size='9px', padding='1px')

# imgkit.from_string(html_table, "tgbot/pictures/goalpas.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/goalpas.png"])


# def SWHL_penalties():
#     url = "https://swhl.ru/tournament/1033299/stats/penalties?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_penalties(), 'blue_dark',
#                          text_align='left', font_size='13px', padding='4px')

# imgkit.from_string(html_table, "tgbot/pictures/penalties.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/penalties.png"])


# def SWHL_best():
#     url = "https://swhl.ru/tournament/1033299/stats/best-players?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_best(), 'blue_dark',
#                          text_align='left', font_size='20px', padding='7px')

# imgkit.from_string(html_table, "tgbot/pictures/best.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/best.png"])


# def SWHL_goalkeepers():
#     url = "https://swhl.ru/tournament/1033299/stats/goalkeepers?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_goalkeepers(), 'blue_dark',
#                          text_align='left', font_size='20px', padding='7px')

# imgkit.from_string(html_table, "tgbot/pictures/goalkeepers.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/goalkeepers.png"])


# def SWHL_saltworts():
#     url = "https://swhl.ru/tournament/1033299/stats/saltworts?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_saltworts(), 'blue_dark',
#                          text_align='left', font_size='20px', padding='7px')

# imgkit.from_string(html_table, "tgbot/pictures/saltworts.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/saltworts.png"])


# def SWHL_teams():
#     url = "https://swhl.ru/tournament/1033299/stats/teams-common?common=1"
#     response = requests.get(url)
#     df_list = pd.read_html(response.text)

#     return df_list[0]


# html_table = build_table(SWHL_teams(), 'blue_dark',
#                          text_align='left', font_size='20px', padding='7px')

# imgkit.from_string(html_table, "tgbot/pictures/teams.png", options={
#                    'format': 'png', 'encoding': "UTF-8"})

# subprocess.Popen(
#     ["xdg-open", "tgbot/pictures/teams.png"])
