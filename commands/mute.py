import discord
from discord.ext import commands


class Mute:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member=None):
        """
        To-do: Everything
        :param ctx:
        :param user:
        :return:
        """
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return


def setup(bot):
    bot.add_cog(Mute(bot))
