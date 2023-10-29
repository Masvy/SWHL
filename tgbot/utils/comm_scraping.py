from bs4 import BeautifulSoup


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def commands(url, session):
    commands_list = []
    page = await fetch(url, session)
    soup = BeautifulSoup(page, 'lxml')
    commands = soup.find_all('span', class_='table__team-name')
    for command in commands:
        commands_list.append(f'🏒{command.text}🏒')
    return commands_list


async def urls(url, session):
    url_list = []
    page = await fetch(url, session)
    soup = BeautifulSoup(page, 'lxml')
    commands_url = soup.find_all('a', class_='table__team')
    for urls in commands_url:
        url = urls.get('href')
        url_list.append(f"http://www.swhl.ru{url}")
    return url_list
