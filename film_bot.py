from telegram.ext import Updater , CommandHandler , MessageHandler, Filters

import logging
import settings

from handlers import *


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("films", films))
    #dp.add_handler(CommandHandler("film", film))
    dp.add_handler(CommandHandler("123", film_base, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__=='__main__':
    main()