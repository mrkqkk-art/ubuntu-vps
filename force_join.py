from config import CHANNELS


async def check_membership(bot, user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(
                chat_id=channel,
                user_id=user_id
            )

            if member.status in ["left", "kicked"]:
                return False

        except Exception as e:
            print("Force join error:", e)
            return False

    return True
