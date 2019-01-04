import discord
import asyncio
import re
from discord.ext import commands
from IcyBot.Utils.error_embeds import EmbedBuilder


def time_convert(time_string):
    if not re.match(r"^((\d+d)?(\d+h)?(\d+m)?(\d+s)?)$", time_string):
        return print("Invalid format")
    time_string = time_string.replace("d", "*86400")
    time_string = time_string.replace("h", "*3600")
    time_string = time_string.replace("m", "*60")
    time_string = time_string.replace("s", "")
    return eval(time_string)


class Mute:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member = None, *, args):
        """
        To-do: Everything
        :param ctx:
        :param user:
        :return:
        """
        args = args.split(" ")
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        #if user is ctx.author or user is None:
           # return
        if not args:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Something went wrong!", "Please specify arguments"), delete_after=4)
        try:
            mute_role = next(r for r in ctx.guild.roles if r.name == "Muted")
        except StopIteration as err:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Something went wrong!", "I could not find the specified mute role!"), delete_after=4)
        mute_time = time_convert(args[0])
        await user.add_roles(mute_role)

        await asyncio.sleep(mute_time)

        return await user.remove_roles(mute_role)


def setup(bot):
    bot.add_cog(Mute(bot))
