from config import CHANNELS


async def check_membership(bot, user_id):

    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(
                channel,
                user_id
            )

            if member.status in ["left", "kicked"]:
                return False

        except:
            return False

    return True
