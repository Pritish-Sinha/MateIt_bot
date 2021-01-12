import logging
import Lichess
import telegram
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1599459387:AAHrlvU-r2-2T-KNHu419WcgnR_ZRBFjn50"

URL = " https://lichess.org/api/"


def start(bot, update):
    
    update.message.reply_text("Welcome let's Mate it")


def help(bot, update):
    


    update.message.reply_text(
        'These are the commands you can use\n'
        '/start - Greets you with Hello\n'
        '/help - Display available commands\n'
        '/profile <username> - Display information about a lichess user\n'
        '/online <username(s), separated by comma> - Check if user(s) \
            are online or not\n'
        '/top <chess variant> - Display top 10 player for particular variant\n'
        '/stream - Display all live streamer on lichess\n'

    )


def error(bot, update, error):
   
    logger.warning('Update "%s" caused error "%s"', update, error)


def user(bot, update, args):
   
    profile = Lichess.profile(args)
    update.message.reply_text(profile, parse_mode=telegram.ParseMode.HTML)


def online(bot, update, args):
    
    args = "".join(args)
    online = Lichess.is_online(args)
    update.message.reply_text(online, parse_mode=telegram.ParseMode.HTML)


def top_players(bot, update, args):
   
    args = "".join(args)
    update.message.reply_text(Lichess.top_players(args),
                              parse_mode=telegram.ParseMode.HTML)


def streamer(bot, update):
   

    update.message.reply_text(Lichess.streamers(),
                              parse_mode=telegram.ParseMode.HTML)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("profile", user, pass_args=True))
    dp.add_handler(CommandHandler("online", online, pass_args=True))
    dp.add_handler(CommandHandler("top", top_players, pass_args=True))
    dp.add_handler(CommandHandler("stream", streamer))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()

