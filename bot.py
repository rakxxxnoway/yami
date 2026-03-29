from pathlib import Path
import json
import time
import os
###
import telebot
from telebot import types
from dotenv import load_dotenv
###
import libs.collection  as collection
import libs.bigdata     as bigdata
import libs.animals     as animals
import libs.recipe      as recipe
import libs.social      as social
import libs.movie       as movie
import libs.msk         as msk
import libs.mks         as mks
import libs.teso        as teso
import libs.weather     as weather
import libs.settings    as user_settings
import libs.downloader  as downloader


################---GLOBALS---############################
e_path = Path(__file__).parent / "data" / "data.env"    #
load_dotenv(dotenv_path=e_path)                         #
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))           #
loh = bigdata.rand_list(collection.us)                  #
pcat = "data/cats.yaml"                                 #
#########################################################


####################---COMMANDS---####################
@bot.message_handler(commands=["start"])
def start(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    mrk.add(btn1)
    bot.send_message(msg.from_user.id, "Привет, Кать или Госька\nЧем могу служить сегодня?")
    bot.send_message(msg.from_user.id, "Вот меню: /menu")


####################---Menu---####################
@bot.message_handler(commands=["menu"])
def menu(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Повседневка👩‍❤️‍👨")
    btn2 = types.KeyboardButton("Игры🎲")
    btn3 = types.KeyboardButton("Важно💯")
    btn4 = types.KeyboardButton("Шутки-хуютки😹")
    btn5 = types.KeyboardButton("Анал из😧")
    btn6 = types.KeyboardButton("Кисиски🐈")
    btn7 = types.KeyboardButton("Что нового?📰")

    mrk.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(msg.from_user.id, "Выбирай хуле", reply_markup=mrk)


####################---1---####################
@bot.message_handler(commands=["yamy"])
def yamy(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поболтать💬")
    btn2 = types.KeyboardButton("Что будем смотреть?🎞️")
    btn3 = types.KeyboardButton("Что сегодня готовить?🍲")
    btn4 = types.KeyboardButton("Инфаℹ️")
    btn5 = types.KeyboardButton("Космос🚀")
    btn6 = types.KeyboardButton("Погода🌥️")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(btn4, btn6, btn2, btn3, btn5, btn1, ext)
    bot.send_message(msg.from_user.id, "Держите, мои любимки", reply_markup=mrk)


####################---2---####################
@bot.message_handler(commands=["puksrenk"])
def puksrenk(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Монетка🟡")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(btn1, ext)
    bot.send_message(msg.from_user.id, "Держите, мои любимки", reply_markup=mrk)


####################---3---####################
@bot.message_handler(commands=["usuka"])
def usuka(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Цены на такси🚕")
    btn2 = types.KeyboardButton("TESO Сервера🎲")
    btn3 = types.KeyboardButton("Скачать видео🎥")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(btn1, btn2, btn3, ext)
    bot.send_message(msg.from_user.id, "Держите, мои любимки", reply_markup=mrk)


####################---4---####################
@bot.message_handler(commands=["anal"])
def anal(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Напоминалка🤓")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(btn1, ext)
    bot.send_message(msg.from_user.id, "Держите, мои любимки", reply_markup=mrk)

@bot.message_handler(commands=["pamyatynet"])
def pamyatynet(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить➕")
    btn2 = types.KeyboardButton("Удалить➖")
    btn3 = types.KeyboardButton("Посмотреть✔️")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(btn1, btn2, btn3, ext)
    bot.send_message(msg.from_user.id, "Держите, мои любимки", reply_markup=mrk)


####################---5---####################
@bot.message_handler(commands=["kisk", "kisa", "muzhoska", "katuska"])
def kisk(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Случайный кись🙀")
    #bt2 = types.KeyboardButton("Полистать кись🐅")
    bt3 = types.KeyboardButton("Поиск кись🙀")
    ext = types.KeyboardButton("Назад🔙")

    mrk.add(bt1, bt3, ext)
    bot.send_message(msg.from_user.id, "Мур Мур", reply_markup=mrk)



####################---TEXT RESPONSE---####################
@bot.message_handler(content_types=["text"])
def get_text_messages(msg):
    try:
        # повседневка /yamy
        if msg.text == "Повседневка👩‍❤️‍👨":
            bot.send_message(msg.from_user.id, "/yamy")
        
        elif msg.text.lower() in ("инфаℹ️", "инфа", "ямы"):
            bot.send_message(msg.from_user.id, msk.info_date(msk.get_time_data(msk.SPB), msk.get_time_data(msk.KAR), loh, collection.really_bad_jokes), parse_mode="Markdown")
            
            pic_url = "https://i.ibb.co/nsNpKRsw/9MA7b8d.jpg"

            """
            https://i.ibb.co/Mxpj65YY/VTHLPvY.jpg     - kat
            https://i.ibb.co/zkMq0h3/Em5Z2e6.jpg      - gre
            https://i.ibb.co/nsNpKRsw/9MA7b8d.jpg     - non
            """

            match loh:
                case "Катька":
                    pic_url = "https://i.ibb.co/Mxpj65YY/VTHLPvY.jpg"
                case "Госька":
                    pic_url = "https://i.ibb.co/zkMq0h3/Em5Z2e6.jpg"
                case _:
                    pic_url = "https://i.ibb.co/nsNpKRsw/9MA7b8d.jpg"
            
            bot.send_photo(msg.from_user.id, pic_url)
            
        elif msg.text.lower() in ("погода🌥️", "погода", "пг"):
            bot.send_message(msg.from_user.id, weather.parse_data(weather.get_weather_data(weather.SPB), weather.get_weather_data(weather.KAR)), parse_mode="Markdown")

        elif msg.text == "Космос🚀":
            bot.send_message(msg.from_user.id, mks.info_mks(mks.get_mks_data(mks.MKS)), parse_mode="Markdown")

        elif msg.text == "Поболтать💬":
            bot.send_message(msg.from_user.id, f"Да хуле мне с вами пиздеть сейчас? Зянят я! Иди вон, напишите лучше друг другу\nХотя, могу вот только вопрос придумать...\n*{social.to_ask()}*", parse_mode="Markdown")
        
        elif msg.text == "Что будем смотреть?🎞️":
            bot.send_message(msg.from_user.id, f"*В душе не ебу, но я подумаю над этим вопросом\nА хотя нет...\n{movie.to_watch()}*", parse_mode="Markdown")
        
        elif msg.text == "Что сегодня готовить?🍲":
            bot.send_message(msg.from_user.id, f"*{recipe.to_eat()}*", parse_mode="Markdown")
        

        # игры /puksrenk
        elif msg.text == "Игры🎲":
            bot.send_message(msg.from_user.id, f"*Бляя, я хз пока во что вам сыграть. Вон, идите лучше в It takes Two или команда:\n/puksrenk*", parse_mode='Markdown')
        
        elif msg.text == "Монетка🟡":
            bot.send_message(msg.from_user.id, bigdata.rand_list(collection.monetka), parse_mode="Markdown")
        

        # важное /usuka
        elif msg.text == "Важно💯":
            bot.send_message(msg.from_user.id, "Нихуя ты важный /usuka", parse_mode="Markdown")
        
        #TESO Сервера🎲
        elif msg.text == "TESO Сервера🎲":
            bot.send_message(msg.from_user.id, teso.parse_stat(teso.get_status(teso.URL_STATUS)), parse_mode="Markdown")

        #Скачать видео🎥
        elif msg.text == "Скачать видео🎥":
            url_ = bot.send_message(msg.from_user.id, "🎞️ Ссылочку пожалуйста...")
            bot.register_next_step_handler(url_, send)

        elif msg.text == "Цены на такси🚕":
            bot.send_message(msg.from_user.id, f"*Сами гляньте, у мня нет времени!\n\nP.S.\nГоська просто лох и не может добавить функцию ыыы*", parse_mode="Markdown")


        elif msg.text == "Настройки⚙️":
            # https://i.ibb.co/1fWGJsFf/nJrnPH7.jpg
            purl = "https://i.ibb.co/1fWGJsFf/nJrnPH7.jpg"

            bot.send_photo(msg.from_user.id, purl)
            bot.send_message(msg.from_user.id, f"/settings", parse_mode="Markdown")

        elif msg.text == "Интервал напоминаний〰️":
            interv = bot.send_message(msg.from_user.id, f"Введите значение (минуты)")
            bot.register_next_step_handler(interv, interval)



        # шутки /xd
        elif msg.text == "Шутки-хуютки😹":
            # https://i.ibb.co/hR3XLng6/CZr0CpN.jpg
            bot.send_photo(msg.from_user.id, "https://i.ibb.co/hR3XLng6/CZr0CpN.jpg")
            bot.send_message(msg.from_user.id, "Ну как? Смешно? Ну поплачь", parse_mode="Markdown")


        # анал из /anal
        elif msg.text == "Анал из😧":
            bot.send_message(msg.from_user.id, "Лови /anal")
        
        elif msg.text == "Напоминалка🤓":
            bot.send_message(msg.from_user.id, "Эх, дырявая башка, лови: /pamyatynet")
        
        elif msg.text == "Добавить➕":
            rem = bot.send_message(msg.from_user.id, "Нуу, и чего мне надо запомнить?")
            bot.register_next_step_handler(rem, remem)
        
        elif msg.text == "Удалить➖":
            del_ = bot.send_message(msg.from_user.id, "Нуу, и чего мне надо удалить?")
            bot.register_next_step_handler(del_, delete)
        
        elif msg.text == "Посмотреть✔️":
            try:
                with open("data/data.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("[!]: File data.json not found!")
                return
            
            if data:
                for block in data:
                    bot.send_message(msg.from_user.id, f"{bigdata.ttemoji(str(block['id']))} {block['text'].replace('!', '')}")
            else:
                print("[!]: File's empty!")
                bot.send_message(msg.from_user.id, f"Пустяяя")



        # Кисы
        elif msg.text == "Кисиски🐈":
            bot.send_message(msg.from_user.id, "Мяу😽 /kisk", parse_mode="Markdown")


        elif msg.text == "Случайный кись🙀":
            rid = bigdata.rint(1, 70)
            pic_path = animals.grand_pic(rid)

            with open(pic_path, "rb") as photo:
                bot.send_photo(msg.from_user.id, photo=photo)
            
            bot.send_message(msg.from_user.id, animals.info_cats( animals.load_cat( rid, animals.load_yaml(pcat) ), collection.titles), parse_mode="Markdown")

        elif msg.text == "Полистать кись🐅":
            pass

        elif msg.text == "Поиск кись🙀":
            kis = bot.send_message(msg.from_user.id, "🐈‍⬛И какого кисика ты ищешь?🐈‍⬛", parse_mode="Markdown")
            bot.register_next_step_handler(kis, cat_lookup)

        
        # новости/общие
        elif msg.text == "Что нового?📰":
            bot.send_message(msg.from_user.id, bigdata.motd(), parse_mode="Markdown")
        
        # кнопка назад
        elif msg.text == "Назад🔙":
            bot.send_message(msg.from_user.id, "Воть /menu")

    except Exception as e:
        print(f"[!] Error: {e}")


################---FUNCTIONS---############################
def send(msg):
    url = msg.text

    if not url.startswith(("http://", "https://")):
        m = bot.send_message(msg.from_user.id, "❌ Это не то, попробуй ещё раз")
        bot.register_next_step_handler(m, send)
        return

    bot.send_message(msg.from_user.id, "⏳ Скачиваю...")

    src = downloader.Downloader(url)
    src.clear()
    src.download()

    bot.send_message(msg.from_user.id, "🟢 Скачал, ща скину")

    bot.send_video(msg.from_user.id, open(f"temp/{src.get_name}", "rb"))

    src.clear()

def remem(msg):
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    mtext:str = msg.text

    if data:
        last_id = max(entry["id"] for entry in data)
    else:
        last_id = 0

    if "!!" in mtext:
        mtext = mtext.upper()

    new_block = {"id": last_id + 1, "text": mtext}
    data.append(new_block)

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    bot.send_message(msg.from_user.id, f"Сохранение прошло удачно!")


def delete(msg):
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл data.json не найден.")
        return

    if msg.text.lower() == "всё":
        data = []
        bot.send_message(msg.from_user.id, "Всё удалил)")
    else:
        original_length = len(data)
        data = [block for block in data if block["id"] != int(msg.text)]
        if len(data) < original_length:
            bot.send_message(msg.from_user.id, f"Напоминалка с id *{int(msg.text)}* удалён ыыы", parse_mode="Markdown")
        else:
            bot.send_message(msg.from_user.id, f"Напоминалка с id *{int(msg.text)}* не найден, увы", parse_mode="Markdown")

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def cat_lookup(msg):
    try:
        fcat = animals.look_up( str(msg.text), animals.load_yaml(pcat) )
        pic_path = animals.grand_pic(fcat[0])

        with open(pic_path, "rb") as photo:
            bot.send_photo(msg.from_user.id, photo=photo)

        bot.send_message(msg.from_user.id, animals.info_cats( animals.load_cat( fcat[0], animals.load_yaml(pcat) ), collection.titles), parse_mode="Markdown")

    except Exception as e:
        print(e)


def interval(msg):
    minutes = int(msg.text.strip()) * 60_000
    user_settings

    bot.send_message(msg.from_user.id, f"Интервал изменён на ")



####################---RUNTIME---####################
if __name__ == "__main__":
    try:
        print("[*] Bot started!")
        bot.polling(non_stop=True, interval=0)

    except Exception as e:
        print(f"[i]: {e}")
        #time.sleep(10)
