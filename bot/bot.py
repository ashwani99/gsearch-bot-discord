from discord.ext.commands import Bot
from settings import DISCORD_TOKEN, BOT_COMMAND_PREFIX


bot = Bot(command_prefix=BOT_COMMAND_PREFIX, case_insensitive=True)

bot.load_extension('cogs.greeting')
bot.load_extension('cogs.googlesearch')


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
