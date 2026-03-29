import json
import pickle
import random


def motd() -> str:
    # 🟡
    # 🟢
    return f"""
*📜Обновление от: 22/08/2025📜*
--------------------------------
✅Добавленно:
    🟢 Кнопка *Настройки⚙️* в секции *Важно💯*

🛠️Изменено:
    🟡 Визуальный стиль:
    🟡 🟡 ID сообщения изменено на соответвующие эмодзи
    
    🟡 Функционал:
    🟡 🟡 Добавлено сообщение что напоминание добавлено успешно
    🟡 🟡 Добавлена функция важных сообщений. При добавлении напоминания, добавте два или больше восклицательных знаков в любом месте (не будут отображаться при просмотре)
    🟡 🟡 Добавлен интервал частоты напоминания важных сообщений
    🟡 🟡 Интервал можно настроить через *Настройки⚙️*
"""

# orig
"""
*📜Обновление от: 23/06/2025📜*
--------------------------------
✅Добавленно:
    🟢 

🛠️Изменено:
    🟡 
"""

def rand_list(lst:list) -> str:
    lohotron = []

    for i in range(0, 10):
        lohotron.append(lst[i%len(lst)])

    random.shuffle(lohotron)

    return random.choice(lohotron)


def rint(a, b) -> int : return random.randint(a, b)


def get_month(val) -> str:
    months = ["января", "февраля", "марта", "апреля", "майя", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    return months[int(val)-1]


def dtemoji(char:str) -> str:
    digits_to_emoji = {
        "0":    "0️⃣",
        "1":    "1️⃣",
        "2":    "2️⃣",
        "3":    "3️⃣",
        "4":    "4️⃣",
        "5":    "5️⃣",
        "6":    "6️⃣",
        "7":    "7️⃣",
        "8":    "8️⃣",
        "9":    "9️⃣",
        "10":   "🔟",
    }

    return digits_to_emoji[char]


def ttemoji(number:str) -> str:
    rnum = []
    for c in str(number):
        rnum.append(dtemoji(c))

    return " ".join(rnum)


def load_file(f_name:str) -> dict:
    try:
        with open(f_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!]: File data.json not found!")
        return


def save_file(f_name:str, data:dict) -> None:
    with open(f_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
