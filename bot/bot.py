import random

from discord.ext import commands
from googlesearch import search

from settings import DISCORD_TOKEN, BOT_COMMAND_PREFIX

bot = commands.Bot(command_prefix=BOT_COMMAND_PREFIX, case_insensitive=True)

@bot.command(name='hey')
async def hey_response(ctx):
    await ctx.send(f'Hi' {ctx.author.name} :wave:)


@bot.command(name='google')
async def google_search(ctx, query: str):
    await ctx.send('Hold on! Fetching search results for you...')
    async with ctx.channel.typing():
        results = search(query, stop=5)
        await ctx.send(f' You are {ctx.author.name} :laughing:')
        await ctx.send('\n'.join(results))


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
