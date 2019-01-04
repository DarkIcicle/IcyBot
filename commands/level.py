import discord
from discord.ext import commands
from IcyBot.bot import con
from IcyBot.Utils.error_embeds import EmbedBuilder


class Level:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def level(self, ctx, user: discord.Member=None):
        if con.connection is None:
            return await ctx.channel.send(embed=EmbedBuilder().no_connection(), delete_after=3)

        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is None:
            user = ctx.author
        con.create_user(user.id, user.name)
        level_embed = discord.Embed(title="{}'s level".format(user.name), description=str(con.get_level(user.id)), color=0xFFB200)
        level_embed.add_field(name="EXP to next", value="`{}`".format(100*con.get_level(user.id)-con.get_experience(user.id)))
        level_embed.set_thumbnail(url=user.avatar_url)
        await ctx.message.channel.send(embed=level_embed)


def setup(bot):
    bot.add_cog(Level(bot))