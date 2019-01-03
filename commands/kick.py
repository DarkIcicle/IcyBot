import discord
from discord.ext import commands


class Kick:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is None:
            return
        kick_reason = ctx.message.slice(2)
        await ctx.message.channel.say(":boot: So long {}.".format(user.name))
        await user.kick(reason=kick_reason)


def setup(bot):
    bot.add_cog(Kick(bot))
