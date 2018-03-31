# -*- coding: utf-8 -*-
import logging

from decouple import config
from emoji import emojize
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

from utils import md5, aestheticize
import constants

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vprw")

# Load config
CONFIG = {
    "BOT_TOKEN": config("BOT_TOKEN")
}


def start_handler(bot, update):
    """
    /start command handler
    :param bot:
    :param update:
    :return:
    """
    response_text = emojize(":sparkles::dizzy: ")
    response_text += aestheticize("vprw bot!\n_Made by nyo_ ", symbols=False)
    response_text += "(@asyncdef)"
    response_text += aestheticize(emojize(" _in :snake:_"))
    response_text += "\nThis is a little inline python telegram bot i made to " \
                     "aestheticize your telegram messages.\n\n"
    response_text += emojize(":waning_crescent_moon: *Usage*\n", use_aliases=True)
    response_text += "`@{} your message`\n".format(bot.username)
    response_text += emojize(" " * 18 + ":point_down:\n", use_aliases=True)
    response_text += "`" + aestheticize("your message") + "`"
    response_text += emojize("\n\n:yellow_heart: *Cool stuff*\n")
    response_text += emojize(":point_right: [My website](https://nyodev.xyz)\n", use_aliases=True)
    response_text += emojize(":point_right: [My GitHub profile](https://github.com/xNyo)\n", use_aliases=True)
    response_text += emojize(":point_right: [vprw source code](https://github.com/xNyo/vprwbot)", use_aliases=True)
    response_text += aestheticize("\n\n_Quante cose al mondo puoi fare..._")
    update.message.reply_text(response_text, parse_mode="markdown", disable_web_page_preview=True)


def inline_query_handler(bot, update):
    """
    Inline query handler
    :param bot:
    :param update:
    :return:
    """
    query = update.inline_query.query

    # Build various aesthetic responses
    aesthetic_contents = [
        aestheticize(query),
        aestheticize(query, spaced=True),
        aestheticize(query.upper()),
        aestheticize(query.upper(), spaced=True),
        aestheticize(query.lower()),
        aestheticize(query.lower(), spaced=True),
    ]

    # Send results
    update.inline_query.answer([
        InlineQueryResultArticle(
            id=md5(x),
            title=x,
            input_message_content=InputTextMessageContent(x)
        ) for x in aesthetic_contents
    ])


def error(bot, update, error):
    """
    Error handler
    :param bot:
    :param update:
    :param error:
    :return:
    """
    logger.warning("Update '%s' caused error '%s'", update, error)


def main():
    """
    Main method
    :return:
    """
    print(aestheticize("vprw @ {}".format(constants.VERSION), symbols=False))
    print(aestheticize("made by nyo", symbols=False))
    print()

    updater = Updater(CONFIG["BOT_TOKEN"])
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(InlineQueryHandler(inline_query_handler))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    logger.info(aestheticize("Bot started!"))
    updater.idle()


if __name__ == "__main__":
    main()
