import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8996305506:AAG21VlDla-DB3IAmV5MKHt5F34wySgltYA"
CHANNEL = "@SardorBroGames"

bot = telebot.TeleBot(TOKEN)

# ─── MENU ───
def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton("ℹ️ Biz haqimizda"),
        KeyboardButton("💡 Maslahat berish")
    )

    markup.add(
        KeyboardButton("🎮 O‘yinlar")
    )

    return markup

# ─── START ───
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Xush kelibsiz SardorBro Botga 🤖",
        reply_markup=menu()
    )

# ─── ABOUT ───
@bot.message_handler(func=lambda m: m.text == "ℹ️ Biz haqimizda")
def about(message):
    bot.send_message(
        message.chat.id,
        "🔥 SardorBro Jamoasi\n\n"
        "Biz o‘yinlar yaratamiz va obunachilarga taqdim etamiz.\n\n"
        "👤 Admin: @SardorBro645"
    )

# ─── MASLAHAT ───
@bot.message_handler(func=lambda m: m.text == "💡 Maslahat berish")
def ask_advice(message):
    msg = bot.send_message(
        message.chat.id,
        "✍️ Maslahatingizni yozing:\nU avtomatik kanalga yuboriladi."
    )
    bot.register_next_step_handler(msg, send_advice)

def send_advice(message):
    user = message.from_user
    username = f"@{user.username}" if user.username else "yo‘q"

    bot.send_message(
        CHANNEL,
        f"💡 Yangi maslahat:\n\n"
        f"👤 Ism: {user.first_name}\n"
        f"🔗 Username: {username}\n"
        f"🆔 ID: {user.id}\n\n"
        f"💬 Xabar: {message.text}"
    )

    bot.send_message(message.chat.id, "✅ Maslahat yuborildi!")

# ─── O‘YINLAR ───
@bot.message_handler(func=lambda m: m.text == "🎮 O‘yinlar")
def games(message):
    bot.send_message(
        message.chat.id,
        "🎮 Hozircha o‘yinlar yo‘q.\n"
        "📌 Keyin @SardorBroGames kanalida chiqadi."
    )

# ─── DEFAULT ───
@bot.message_handler(func=lambda m: True)
def unknown(message):
    bot.send_message(
        message.chat.id,
        "⚠️ Men faqat menyu orqali ishlayman.\n/start ni bosing."
    )

print("🤖 Bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)