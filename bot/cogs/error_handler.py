from discord.ext.commands import Cog, errors

class ErrorHandler(Cog):
    """ Generic error handler for commands emitted errors """

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, e):
        """ Generic event listener for all errors """

        command = ctx.invoked_with

        if isinstance(e, errors.MissingRequiredArgument):
            await ctx.send(f'Oh! It seems you have forgot required argument `{e.param.name}` ¯\_(ツ)_/¯')
            await ctx.send_help(command)
        elif isinstance(e, errors.TooManyArguments):
            await ctx.send('Are you rich? These are too many arguments to handle (╯°□°）╯︵ ┻━┻')
            await ctx.send_help(command)
        elif isinstance(e, (errors.BadArgument, errors.BadUnionArgument)):
            await ctx.send(f'Sorry, these are bad argument `{e}`')
            await ctx.send_help(command)
        elif isinstance(e, errors.ArgumentParsingError):
            await ctx.send(f'Arguments are beyond my understanding :face_with_monocle:')
            await ctx.send_help(command)
        elif isinstance(e, errors.UserInputError):
            await ctx.send(f'I am still trying to learn what these arguments mean :pleading_face:')
            await ctx.send_help(command)
        elif not isinstance(e, errors.CommandNotFound):
            await ctx.send(f'Something unexpected happened to me. '
            'Don\'t ell this to my master! :sick:')
            await ctx.send(f'Here is my help command')
            await ctx.send_help()
        

def setup(bot):
    bot.add_cog(ErrorHandler(bot))