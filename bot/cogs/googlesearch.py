from discord.ext import commands
from googlesearch import search

class GoogleSearch(commands.Cog, name='Search on Google'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google')
    async def google_search(self, ctx, query: str):
        """ Finds search results from Google search 
        Usage: !google <query>
        
        Optionally, you can ask for more than 5 results by providing limit
        Usage: !google <query> <limit>

        Examples: 
            !google hello
            !google hello 10
        """
        if query.split(' ')[-1].isnumeric():
            query, limit = query.rsplit(' ', maxsplit=1)
        else:
            limit = 5
            
        await ctx.send(f'{ctx.author.mention} Hold on! Fetching search results for you... :clock:')
        async with ctx.channel.typing():
            results = search(query, stop=limit)

            await ctx.send('\n'.join(results))


def setup(bot):
    bot.add_cog(GoogleSearch(bot))