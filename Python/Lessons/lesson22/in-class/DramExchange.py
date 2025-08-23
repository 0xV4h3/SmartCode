from telebot import TeleBot, types
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading, time
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = TeleBot(TOKEN)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.rate.am/hy/armenian-dram-exchange-rates/banks"

rates = {}
banks_rates = {}
banks_order = []

def to_float(text):
    try:
        return float(text.replace("֏", "").replace(",", "").replace(" ", "").strip())
    except Exception:
        return text.strip()

def update_rates():
    global banks_rates, banks_order
    while True:
        try:
            driver.get(URL)
            time.sleep(2)

            avg_row = driver.find_element(By.CSS_SELECTOR, "div.group.flex.items-center.h-10.bg-N30")
            cols = avg_row.find_elements(By.CSS_SELECTOR, "div.text-center")
            rates.clear()
            rates.update({
                "USD": {"buy": to_float(cols[0].text), "sell": to_float(cols[1].text)},
                "EUR": {"buy": to_float(cols[2].text), "sell": to_float(cols[3].text)},
                "RUR": {"buy": to_float(cols[4].text), "sell": to_float(cols[5].text)}
            })

            banks_rates.clear()
            banks_order.clear()

            parent = driver.find_element(By.CSS_SELECTOR, "div.w-full.grow.rounded-tl-xl")

            bank_blocks = parent.find_elements(By.XPATH, "./div[contains(@class, 'relative')]")

            rate_parent = driver.find_element(By.CSS_SELECTOR, "div.w-full.grow.bg-white")
            rate_blocks = rate_parent.find_elements(By.XPATH, "./div[contains(@class, 'flex') and contains(@class,'bg-white')]")

            for idx in range(min(len(bank_blocks), len(rate_blocks))):
                bank_div = bank_blocks[idx]
                rates_div = rate_blocks[idx]
                try:
                    a_tag = bank_div.find_element(By.CSS_SELECTOR, "span > a")
                    name = a_tag.text.split('\n')[0].strip()
                    slug = name.replace(" ", "_")

                    currency_divs = rates_div.find_elements(By.XPATH, ".//div[contains(@class,'min-w-')]")
                    bank_data = {
                        "name": name,
                        "USD": {"buy": "-", "sell": "-"},
                        "EUR": {"buy": "-", "sell": "-"},
                        "RUR": {"buy": "-", "sell": "-"}
                    }
                    for cur, div in zip(['USD', 'EUR', 'RUR'], currency_divs):
                        cells = div.find_elements(By.XPATH, ".//div[contains(@class,'w-1/2')]")
                        buy = to_float(cells[0].text) if len(cells) > 0 else '-'
                        sell = to_float(cells[1].text) if len(cells) > 1 else '-'
                        bank_data[cur] = {'buy': buy, 'sell': sell}
                    banks_rates[slug] = bank_data
                    banks_order.append(slug)
                except Exception as e:
                    print("Bank block parsing error:", e)
                    continue

            print(f"Rates updated: {rates}")
            print(f"Banks loaded: {len(banks_rates)}")
        except Exception as e:
            print("Error updating rates:", e)
        time.sleep(300)

threading.Thread(target=update_rates, daemon=True).start()

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Average rates", "Banks")
    bot.send_message(message.chat.id, "Welcome! Please choose:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Average rates")
def average_handler(message):
    txt = "Average exchange rates:\n"
    for cur in ["USD", "EUR", "RUR"]:
        r = rates.get(cur, {})
        buy = r.get("buy", "-")
        sell = r.get("sell", "-")
        txt += f"{cur}: Buy {buy} | Sell {sell}\n"
    bot.send_message(message.chat.id, txt)

def paginate_banks(page=0, per_page=8):
    start = page * per_page
    kb = types.InlineKeyboardMarkup(row_width=2)
    for slug in banks_order[start:start+per_page]:
        kb.add(types.InlineKeyboardButton(banks_rates[slug]["name"], callback_data=f"bank:{slug}"))
    nav = []
    if page > 0:
        nav.append(types.InlineKeyboardButton("« Prev", callback_data=f"bank_page:{page-1}"))
    if start+per_page < len(banks_order):
        nav.append(types.InlineKeyboardButton("Next »", callback_data=f"bank_page:{page+1}"))
    if nav:
        kb.row(*nav)
    kb.add(types.InlineKeyboardButton("Close", callback_data="close"))
    return kb

@bot.message_handler(func=lambda m: m.text == "Banks")
def banks_handler(message):
    if not banks_rates:
        bot.send_message(message.chat.id, "Loading banks, please try again later.")
        return
    kb = paginate_banks(page=0)
    bot.send_message(message.chat.id, "Select a bank:", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def on_cb(c):
    data = c.data
    if data == "close":
        try: bot.delete_message(c.message.chat.id, c.message.message_id)
        except: pass
        return
    if data.startswith("bank_page:"):
        page = int(data.split(":")[1])
        kb = paginate_banks(page=page)
        bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=kb)
        return
    if data.startswith("bank:"):
        slug = data.split(":")[1]
        kb = types.InlineKeyboardMarkup(row_width=3)
        for cur in ["USD", "EUR", "RUR"]:
            kb.add(types.InlineKeyboardButton(cur, callback_data=f"currency:{slug}:{cur}"))
        kb.add(types.InlineKeyboardButton("Back to banks", callback_data="banks_back"))
        kb.add(types.InlineKeyboardButton("Close", callback_data="close"))
        bot.edit_message_text(f"Choose currency for\n{banks_rates[slug]['name']}:", c.message.chat.id, c.message.message_id, reply_markup=kb)
        return
    if data == "banks_back":
        kb = paginate_banks(page=0)
        bot.edit_message_text("Select a bank:", c.message.chat.id, c.message.message_id, reply_markup=kb)
        return
    if data.startswith("currency:"):
        _, slug, cur = data.split(":")
        rate = banks_rates[slug][cur]
        buy = rate.get("buy", "-")
        sell = rate.get("sell", "-")
        txt = f"{banks_rates[slug]['name']} – {cur}\nBuy: {buy}\nSell: {sell}"
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton("Back to currencies", callback_data=f"bank:{slug}"))
        kb.add(types.InlineKeyboardButton("Back to banks", callback_data="banks_back"))
        kb.add(types.InlineKeyboardButton("Close", callback_data="close"))
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=kb)
        return

bot.infinity_polling()