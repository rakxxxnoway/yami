from playwright.sync_api import sync_playwright


MKS = "https://flug-radar.com/en/isstracker"


def info_mks(data:dict) -> str:
    f_text = f"""
╔═━━◇ [🛰 СТАТУС МКС] ◇━━═╗
┃ 🧬 СИСТЕМА: *МКС / ISS – В СЕТИ*
┃ ⏱ ВРЕМЯ НА ОРБИТЕ: {data['orb'][0]}д {data['orb'][2]}ч {data['orb'][4]}м
┃
┃ 📡 ТЕКУЩИЕ КООРДИНАТЫ:
┃   ➤ Широта: {data['lat']}
┃   ➤ Долгота: {data['lon']}
┃
┃ ⚙️ ОРБИТАЛЬНЫЕ ПАРАМЕТРЫ:
┃   ➤ Высота: {data['alt'][0]} км
┃   ➤ Скорость: {data['v'][0]} км/ч
┃   ➤ Скорость: {round(float(data['v'][0]) / 3.6, 2)} м/с
┃
┃ 👥 ЭКИПАЖ НА БОРТУ: [{len(data['pil'])}] активных участника(ов)
╚═━━◇ [СИГНАЛ: УСТАНОВЛЕН] ◇━━═╝
"""
    s_text = "".join(f"-🧑‍🚀*{pil}*\n" for pil in data["pil"])
    
    return f_text+s_text


def get_mks_data(url:str) -> dict:
    with sync_playwright() as p:
        brw = p.chromium.launch(headless=True)
        page = brw.new_page()
        page.goto(url)

        data = {
            # широта
            "lat": page.locator("#lat_dd").inner_text(),
            # долгота
            "lon": page.locator("#lon_dd").inner_text(),
            # высота
            "alt": page.locator("#altitude_km").inner_text().split(),
            # скорость (km/h) list
            "v": page.locator("#speed_kmh").inner_text().split(),
            # на орбите
            "orb": page.locator("#in_orbit_since").inner_text().split(),
            # экипаж
            "pil": [el.inner_text() for el in page.locator("._astroname").all()]
        }

        brw.close()
        return data


# debug
def print_data(data:dict) -> None:
    print(f"""
Широта: {data['lat']}
Долгота: {data['lon']}
Высота: {data['alt'][0]}
Скорость: {data['v'][0]}
На орбите: {data['orb']}
""")
