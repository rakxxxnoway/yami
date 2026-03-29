import requests
from bs4 import BeautifulSoup
import random
import pickle

SPB = "https://www.timeserver.ru/cities/ru/saint-petersburg"
KAR = "https://www.timeserver.ru/cities/se/karlstad"

temp = {"lvl": 0, "exp": 0, "mexp": 10}
loh_rank = ["Лохосёнок", "Лох", "Лохопет", "Лохозавр", "Мега-Лох", "Ультра-Лох", "Просто Ебать Какой Лох", "Мастер Лох", "Ебанусь Какой Лох"]


def info_date(spb:dict, kar:dict, loh:str, jokes:str) -> str:
    time_s = int(spb['ss'][0:2])-int(spb['h'])
    time_k = int(kar['ss'][0:2])-int(kar['h'])
    #┃ 💯 Лохозвание - *{lrank(lprofile(loh)['lvl'])}* (до следуещего звания {} очков)
    return f"""
╭━💌 *Приветик, любимочка!* 💌━╮
┃ 📅 Сегодня — *{spb['wd']}*, {spb['d']}
┃ 🏆 А звание *Главного Лоха дня* получает: *{loh}* 🎉
┃ 🔁 По счёту это уже неделя № *{int(spb['wn'])}*
╰━━━━━━━━━━━━━━━━╯

🕰 *Текущее время по координатам сердечек:*
┃ ❤️ СПБ: *{spb['h']}:{spb['m']}*
┃ 💙 Карлстад: *{kar['h']}:{kar['m']}*

🌄 *Солнечные прогнозы от ИИ-метеоролога:*
┃ ☀️ В СПБ восход в *{spb['sr']}*
┃   (на {abs(int(str(spb['sr'])[0:2]) - int(str(kar['sr'])[0:2]))} ч. 
┃   { "позже" if int(spb['sr'][0:2]) > int(kar['sr'][0:2]) else "раньше"} чем в Карлстаде)
┃ 🌑 Закат в:
┃   ▸ СПБ — через *{time_s if time_s >= 0 else 24+time_s}* ч.
┃   ▸ Карлстад — через *{time_k if time_k >= 0 else 24+time_k}* ч.

💬 *Лига Плохих Шуток:*
«{random.choice(jokes)}»

🚀 Хочешь вместе полететь в космос?
📲 Жми ➡️ *Космос* 🚀
"""

def get_time_data(url:str) -> dict:
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        data = {
            # hour
            "h": soup.find("span", class_="hours").text.strip(),
            # minutes
            "m": soup.find("span", class_="minutes").text.strip(),
            #week day
            "wd": soup.find("span", attrs={"x-text": "city.week_day"}).text.strip(),
            # date
            "d": soup.find("span", attrs={"x-text": "city.date"}).text.strip(),
            # week num
            "wn": soup.find("span", attrs={"x-text": "city.week_num"}).text.strip(),
            # sunrise
            "sr": soup.find("span", attrs={"x-text": "city.sunrise"}).text.strip(),
            # sunset
            "ss": soup.find("span", attrs={"x-text": "city.sunset"}).text.strip(),
        }

        return data
    else: return None


def lprofile(file_name:str) -> dict:
    with open(f"data/profile/{file_name}.dat", "rb") as f:
        return pickle.load(f)


def lvl() -> None:
    pass



def sprofile(data:dict, file_name:str) -> None:
    ddump = {
        "lvl": data["lvl"],
        "exp": data["exp"],
        "mexp": data["mxp"]
    }
    
    with open(f"data/profile/{file_name}.dat", "wb") as f:
        pickle.dump(ddump, f)


def lrank(lvl:int) -> str : return loh_rank[lvl]


# debug
def print_data(data:dict) -> None:
    print(f"""
Сегодня y нас по МСК {data['wd']}, {data['d']}, неделя {int(data['wn'])}
Время: {data['h']}:{data['m']}
Восход в {data['sr']}
Закат в {data['ss']}
    """)
