from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from config import BOT_TOKEN
from database import (
    create_tables,
    add_user
)

from admin_panel import (
    admin_menu,
    stats
)

from broadcast import broadcast

from buttons import main_buttons

from force_join import check_membership



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    if not await check_membership(
        context.bot,
        user.id
    ):
        await update.message.reply_text(
            "❌ ابتدا عضو کانال شوید:\n@RoXeT_VpN"
        )
        return


    add_user(user.id)


    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات خوش آمدید",
        reply_markup=main_buttons()
    )



async def admin(update: Update, context):

    await admin_menu(
        update,
        context
    )



app = Application.builder().token(
    BOT_TOKEN
).build()



create_tables()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    CommandHandler(
        "admin",
        admin
    )
)


app.add_handler(
    CommandHandler(
        "send",
        broadcast
    )
)


app.add_handler(
    CallbackQueryHandler(
        stats,
        pattern="stats"
    )
)


print("Mirza Bot Started")


app.run_polling()
