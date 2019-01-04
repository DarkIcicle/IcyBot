import discord
from discord.ext import commands
from IcyBot.Utils.error_embeds import EmbedBuilder
from IcyBot.bot import con


class Coins:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coins(self, ctx, user: discord.Member=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if con.connection is None:
            return await ctx.channel.send(embed=EmbedBuilder().no_connection(), delete_after=4)

        if user is None:
            user = ctx.author
        con.create_user(user.id, user.name)
        coin_embed = discord.Embed(title="{}'s coins".format(user.name), description=str(con.get_coins(user.id)),
                                   color=0xFFB200)
        coin_embed.set_thumbnail(url=user.avatar_url)
        await ctx.channel.send(embed=coin_embed)


def setup(bot):
    bot.add_cog(Coins(bot))
