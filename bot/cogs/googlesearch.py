from discord import Embed, Colour
from discord.ext import commands
from googlesearch import search

from store import search_store

class GoogleSearch(commands.Cog, name='Search on Google'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google')
    async def google_search(self, ctx, query: str, limit: int=5):
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
                description='\n'.join(numbered_results) or 'Nothing found :frowning2:',
                colour=Colour.blue()
            )
            search_store.push_search_query(
                guild_id=ctx.guild.id,
                user_id=ctx.author.id,
                query=query
            )
            await ctx.send(embed=embed)

    @commands.command(name='recent')
    async def recent_searches(self, ctx, keyword=None, limit=5):
        """ Displays recent search history 
        
        Usage: !recent [keyword] [limit]

        Optionally, you can provide me with the `keyword` and `limit` of results count.
        By default, top 5 recent search history will be shown. 
        """

        await ctx.send(f'{ctx.author.mention} Let me check on this... :thinking:')
        async with ctx.channel.typing():
            recent_searches = search_store.get_recent_searches(
                guild_id=ctx.guild.id,
                user_id=ctx.author.id,
                keyword=keyword,
                limit=limit
            )
            embed = Embed(
                title=f'{ctx.author.name}\'s recent searches',
                description='\n'.join(recent_searches) or 'Nothing found :frowning2:',
                colour=Colour.blue()
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(GoogleSearch(bot))