from discord.ext import commands

class Greetings(commands.Cog, name='GSearchBot Greetings'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hey")
    async def hey_response(self, ctx):
        """ Greets a user when users greet the bot saying hi/hey/hello etc """
        await ctx.send(f'{ctx.author.mention} Hi {ctx.author.name} :wave: :wave:')

    
def setup(bot):
    bot.add_cog(Greetings(bot))