import discord
from discord.ext import commands
from IcyBot.Utils.error_embeds import EmbedBuilder


class Ban:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, args):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is None:
            return
        args = args.split(" ")
        ban_reason = "".join(args[1:]) if len(args) > 1 else "No reason"
        inc_embed = discord.Embed(colour=discord.Colour.red(),
                                  description="**Kicked by:** {}\n".format(ctx.author.name) +
                                              "**Kicked member:** {}\n".format(user.name) +
                                              "**Reason:** {}\n".format(ban_reason))
        inc_embed.set_author(name="Permanent Ban",
                             icon_url=user.avatar_url if user.default_avatar_url else user.default_avatar_url)
        inc_embed.set_footer(text=ctx.message.created_at)

        inc_chan = next(c for c in ctx.guild.channels if c.name == "incidents")

        await ctx.channel.send(":boot: So long {}.".format(user.name))
        await user.ban()

        if not inc_chan:
            return await ctx.channel.send(embed=EmbedBuilder().custom("Error", "I could not find the specified channel"))

        await inc_chan.send(embed=inc_embed)



def setup(bot):
    bot.add_cog(Ban(bot))
