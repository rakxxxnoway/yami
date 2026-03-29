import random

from bs4 import BeautifulSoup
import requests


KAR = "https://yandex.ru/pogoda/ru/karlstad"
SPB = "https://yandex.ru/pogoda/ru/saint-petersburg"
city = ["Карлстад", "Питер"]

# weather
w = {
    "ливень": "🌧️",
    "дождь": "🌦️",
    "дождь с грозой": "🌩️",
    "облачно": "🌤️",
    "пасмурно": "☁️",
    "ясно": "☀️",
    "снег": "❄️",
    "снег с дождём": "🌨️"
}


# repclis
intro = ["Мурмяу приветик", "Привет любимки", "Кар кар", "Ты лох, да не, прикалываюсь"]


def get_weather_data(url:str) -> dict:
    #AppFactTemperature_sign__1MeN4                             -> sign
    #AppFactTemperature_value__2qhsG                            -> value
    #AppFact_warning__8kUUn                                     -> desc
    #AppFact_feels__IJoel AppFact_feels_withYesterday__yE440    -> feels
    req = requests.get(url)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")
        weather = {
            "city": city[0] if "karlstad" in url else city[1],
            "sign": soup.find("span", class_="AppFactTemperature_sign__1MeN4").text,
            "temp": int( soup.find("span", class_="AppFactTemperature_value__2qhsG").text),
            "feel": soup.find("span", class_="AppFact_feels__IJoel AppFact_feels_withYesterday__yE440").text,
            "desc": soup.find("p", class_="AppFact_warning__8kUUn").text
        }

        return weather

    return {"city": "not found", "sign": "!", "temp": 0}

def parse_data(spb:dict, kar:dict) -> str:
    curr_weather_status_s = ""
    curr_weather_emoji_s  = ""

    curr_weather_status_k = ""
    curr_weather_emoji_k  = ""
    
    for key, val in w.items():
        if key in spb["desc"].lower():
            curr_weather_status_s = key
            curr_weather_emoji_s = val
            break

    for key, val in w.items():
        if key in kar["desc"].lower():
            curr_weather_status_k = key
            curr_weather_emoji_k = val
            break
    

    return f"""
╭━━💌 *{random.choice(intro)}* 💌━━╮
┃ {curr_weather_emoji_s} Погода в {spb['city']}е *{"збс" if spb['temp'] >= 5 and spb['temp'] <= 18 else "ужосная"}* ➡️ Сегодня *{curr_weather_status_s.capitalize()}*
┃ 🌡️ {spb['sign']}{spb['temp']}° - *{spb['desc']}*
┃ 😎 {spb['feel']}
┃
┃ 😏 Тем временем...
┃ {curr_weather_emoji_k} Погода в {kar['city']}е *{"збс" if kar['temp'] >= 5 and kar['temp'] <= 18 else "ужосная"}* ➡️ Сегодня *{curr_weather_status_k.capitalize()}*
┃ 🌡️ {kar['sign']}{kar['temp']}° - *{kar['desc']}*
┃ 😎 {kar['feel']}
╰━━━━━━━━━━━━━━━━╯
"""
