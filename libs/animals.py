import random
from pathlib import Path
import yaml



def info_cats(cat:dict, titles:list) -> str:
    return f"""
╭━━ 😻 *{random.choice(titles)}* 😻 ━╮
┃ 🐾 *Порода:* {cat[1]['name'].capitalize()}
┃ 🎂 *Живёт:* ~{cat[1]['age']} лет мурчания
┃ ⚖️ *Вес:* ≈ {cat[1]['weight']} кг пуха
┃ 📖 *Описулька:*
┃     _{cat[1]['desc'].strip().capitalize()}_
╰━━(=^･ω･^=)━━━━━━━╯
"""


def load_yaml(file_name:str) -> dict:
    with open(file_name, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    

def grand_pic(id:int) -> str:
    folder = Path(f"data/pics/cats/{id}/")

    if not folder.exists() or not folder.is_dir():
        return None

    files = [child for child in folder.iterdir() if child.is_file()]
    if not files:
        return None

    return str(random.choice(files))


def load_cat(id:int, car:dict) -> list:
    cat = []
    
    for key, value in car.items():
        
        if int(key) == id:
            cat.append(id)
            cat.append(value)

    return cat
                

def look_up(name:str, car:dict) -> list:
    cat = []

    for key, value in car.items():
        if name.lower() in value["name"]:
            cat.append(key)
            cat.append(value)

            break

    return cat
