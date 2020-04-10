from discord import Embed, Colour
from discord.ext import commands
from googlesearch import search

class GoogleSearch(commands.Cog, name='Search on Google'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google')
    async def google_search(self, ctx, query: str, limit: int):
        """ Finds search results from Google search 
        Usage: !google <query>
        
        Optionally, you can ask for more than 5 results by providing limit
        Usage: !google <query> <limit>

        Note: Please use quotes(") if you are asking with multiple words. 
        I am dumb to understand without quotes :(

        Examples: 
            !google hello
            !google hello 10
            !google "hello world" 3
        """

        await ctx.send(f'{ctx.author.mention} Hold on! Fetching search results for you... :clock:')
        async with ctx.channel.typing():
            results = search(query, stop=limit)
            numbered_results = [f'{index+1}. {url}' for index, url in enumerate(results)]
            embed = Embed(
                title=f'Search results for `{query}`',
                description='\n'.join(numbered_results),
                colour=Colour.blue()
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GoogleSearch(bot))