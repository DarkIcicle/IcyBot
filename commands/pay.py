import discord
from discord.ext import commands
import asyncio
from TestDiscordBot.bot import con
from TestDiscordBot.Utils.error_embeds import no_connection


class Pay:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pay(self, ctx, user: discord.User=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if con.connection is None:
            return await ctx.channel.send(embed=no_connection())

        payer = ctx.message.author
        try:
            amount = ctx.message.content.split(" ")[2]
            receiver = ctx.message.mentions
        except Exception:
            to_self = discord.Embed(description="Please ensure that you follow the correct format!", color=discord.Color(0).red())
            bot_message = await ctx.channel.send(embed=to_self)
            await asyncio.sleep(2)
            await bot_message.delete()
        if user == payer:
            to_self = discord.Embed(description="You cannot send coins to yourself!", color=discord.Color(0).red())
            bot_message = await ctx.channel.send(embed=to_self)
            await asyncio.sleep(2)
            await bot_message.delete()
        elif con.get_coins(payer) <= amount:
            not_enough = discord.Embed(description="You don't have enough coins!", color=discord.Color(0).red())
            bot_message = await ctx.channel.send(embed=not_enough)
            await asyncio.sleep(2)
            await bot_message.delete()
        else:
            return


def setup(bot):
    bot.add_cog(Pay(bot))
