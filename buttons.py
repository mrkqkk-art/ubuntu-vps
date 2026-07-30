from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_buttons():

    keyboard = [
        [
            InlineKeyboardButton(
                "📢 کانال ما",
                url="https://t.me/RoXeT_VpN"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 پشتیبانی",
                url="https://t.me/ID_RoXeT"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
