import discord
from discord.ext import commands


class Info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, user: discord.Member=None):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        if user is None:
            user = ctx.author

        embed = discord.Embed(title="{}'s info".format(user.name), description="Here's some info I found",
                              color=0x00ff00)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role, inline=True)
        embed.add_field(name="Joined on", value=user.joined_at, inline=True)
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))


