from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import count_users
from config import ADMIN_IDS


def is_admin(user_id):
    return user_id in ADMIN_IDS


async def admin_menu(update, context):

    if not is_admin(update.effective_user.id):
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "📊 آمار کاربران",
                callback_data="stats"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 ارسال همگانی",
                callback_data="broadcast"
            )
        ]
    ]

    await update.message.reply_text(
        "پنل مدیریت:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def stats(update, context):

    query = update.callback_query
    await query.answer()

    users = count_users()

    await query.edit_message_text(
        f"📊 تعداد کاربران: {users}"
  )
