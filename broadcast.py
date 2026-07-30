from database import get_users
from config import ADMIN_IDS


def is_admin(user_id):
    return user_id in ADMIN_IDS


async def broadcast(update, context):

    if not is_admin(update.effective_user.id):
        return

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text(
            "❌ متن پیام را بعد از دستور بنویس\n\nمثال:\n/send سلام به همه"
        )
        return

    users = get_users()

    count = 0

    for user in users:
        try:
            await context.bot.send_message(
                chat_id=user[0],
                text=text
            )
            count += 1

        except:
            pass

    await update.message.reply_text(
        f"✅ پیام برای {count} نفر ارسال شد"
  )
