import os
import sqlite3

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))


db = sqlite3.connect("users.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY
)
""")

db.commit()


def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users(id) VALUES(?)",
        (user_id,)
    )
    db.commit()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    add_user(user.id)

    keyboard = [
        [
            InlineKeyboardButton(
                "کانال ما",
                url="https://t.me/example"
            )
        ]
    ]

    await update.message.reply_text(
        "سلام 👋\nبه ربات خوش آمدید",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    count = cursor.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    await update.message.reply_text(
        f"پنل مدیریت\n\nتعداد کاربران: {count}\n\n"
        "/send متن پیام"
    )


async def send_all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text(
            "متن پیام را بعد از دستور بنویس"
        )
        return


    users = cursor.execute(
        "SELECT id FROM users"
    ).fetchall()


    sent = 0

    for user in users:
        try:
            await context.bot.send_message(
                chat_id=user[0],
                text=text
            )
            sent += 1

        except:
            pass


    await update.message.reply_text(
        f"ارسال شد برای {sent} نفر"
    )



app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("admin", admin)
)

app.add_handler(
    CommandHandler("send", send_all)
)


print("Bot is running...")


app.run_polling()
