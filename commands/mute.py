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
        :param ctx:
        :param user:
        :return:
        """
        args = args.split(" ")
        reason = "".join(args[1:]) if len(args) > 1 else "No reason"
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is ctx.author or user is None:
            return
        if not args:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Something went wrong!",
                                                                      "Please specify arguments"), delete_after=4)
        try:
            mute_role = next(r for r in ctx.guild.roles if r.name == "Muted")
        except StopIteration as err:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Something went wrong!",
                                                                      "I could not find the specified mute role!"),
                                          delete_after=4)
        mute_time = time_convert(args[0])
        await user.add_roles(mute_role)

        inc_embed = discord.Embed(colour=discord.Colour.red(),
                                  description="**Muted by:** {}\n".format(ctx.author.name) +
                                  "**Muted member:** {}\n".format(user.name) +
                                  "**Duration:** {}\n".format(args[0]) +
                                  "**Reason:** {}\n".format(reason))
        inc_embed.set_author(name="Temporary Mute",
                             icon_url=user.avatar_url if user.default_avatar_url else user.default_avatar_url)
        inc_embed.set_footer(text=ctx.message.created_at)

        inc_chan = next(c for c in ctx.guild.channels if c.name == "incidents")
        if not inc_chan:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Error", "I could not find the specified channel"))
        await inc_chan.send(embed=inc_embed)
        await asyncio.sleep(mute_time)

        return await user.remove_roles(mute_role)


def setup(bot):
    bot.add_cog(Mute(bot))
