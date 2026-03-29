from bs4 import BeautifulSoup
import requests


URL_STATUS = "https://esoserverstatus.net/"
SRV_NAMES = ["PC-EU", "PC-NA", "PC-PTS", "XBOX-EU", "XBOX-NA", "PS4-EU", "PS4-NA"]


def get_status(url:str) -> list:
    req = requests.get(url)

    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")

        stats = []

        for srv in SRV_NAMES:
            itm = soup.find("span", {"id": srv})
            stats.append(itm.text)

        return stats

    else: ["error"]


def status(stat:str) -> str:
    if stat == "Offline":   return "🔴"
    else:                   return "🟢"


def parse_stat(data:list) -> str:
    if data[0] == "error":
        return "Ошибка, не установленно соединение!"
    
    return f"""
╔══════════════╗
║   💾 *Статус* 💾   
╠══════════════╣
║   🎛️ _Сервера_ 🎛️   
╠═════PC═══════╣
║   🖥️🇪🇺 ➡️ {status(data[0])}
║   🖥️🇺🇸 ➡️ {status(data[1])}
╠═════XBOX═
║   🎮🇪🇺 ➡️ {status(data[3])}
║   🎮🇺🇸 ➡️ {status(data[4])}
╠═════Playstation═
║   🕹️🇪🇺 ➡️ {status(data[5])}
║   🕹️🇺🇸 ➡️ {status(data[6])}
╠═════Test═Server═
║   🖥️⚒️ ➡️ {status(data[2])}
╚══════════════╝
"""
