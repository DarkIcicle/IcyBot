import discord
from discord.ext import commands


class Ban:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, user: discord.Member=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is None:
            return
        await ctx.channel.send(":boot: So long {}.".format(user.name))
        await user.ban()


def setup(bot):
    bot.add_cog(Ban(bot))
