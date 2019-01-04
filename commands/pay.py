import discord
from discord.ext import commands
import asyncio
from IcyBot.Utils.error_embeds import EmbedBuilder
from IcyBot.bot import con


class Pay:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pay(self, ctx, user: discord.User = None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if con.connection is None:
            return await ctx.channel.send(embed=EmbedBuilder().no_connection(), delete_after=4)

        payer = ctx.message.author
        try:
            amount = ctx.message.content.split(" ")[2]
            receiver = ctx.message.mentions
        except Exception:
            to_self = discord.Embed(description="Please ensure that you follow the correct format!", color=discord.Colour.red())
            return await ctx.channel.send(embed=to_self, delete_after=4)
        if user == payer:
            to_self = discord.Embed(description="You cannot send coins to yourself!", color=discord.Colour.red())
            return await ctx.channel.send(embed=to_self, delete_after=4)
        elif con.get_coins(payer) <= amount:
            not_enough = discord.Embed(description="You don't have enough coins!", color=discord.Colour.red())
            return await ctx.channel.send(embed=not_enough, delete_after=4)
        else:
            return


def setup(bot):
    bot.add_cog(Pay(bot))
