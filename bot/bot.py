import sys

from discord.ext.commands import Bot
from settings import DISCORD_TOKEN, BOT_COMMAND_PREFIX


bot = Bot(command_prefix=BOT_COMMAND_PREFIX, case_insensitive=True)

bot.load_extension('cogs.greeting')
bot.load_extension('cogs.googlesearch')
bot.load_extension('cogs.error_handler')


if __name__ == '__main__':
    if not DISCORD_TOKEN:
        print(
        '''
    No token found for Discord Bot
    
    Please set the bot\'s token using:
    
    export DISCORD_TOKEN=<your-discord-bot-token>
        ''')
        sys.exit()       
        
    bot.run(DISCORD_TOKEN)
