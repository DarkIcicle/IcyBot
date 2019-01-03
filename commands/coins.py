import discord
from discord.ext import commands
from TestDiscordBot.bot import con
from TestDiscordBot.Utils.error_embeds import no_connection


class Coins:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coins(self, ctx, user: discord.Member=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if con.connection is None:
            return await ctx.channel.send(embed=no_connection())

        if user is None:
            user = ctx.author
        con.create_user(user.id, user.name)
        coin_embed = discord.Embed(title="{}'s coins".format(user.name), description=str(con.get_coins(user.id)),
                                   color=0xFFB200)
        coin_embed.set_thumbnail(url=user.avatar_url)
        await ctx.channel.send(embed=coin_embed)


def setup(bot):
    bot.add_cog(Coins(bot))
