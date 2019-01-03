import discord
from discord.ext import commands


class ServerInfo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return
        server_embed = discord.Embed(name="{}'s info".format(ctx.guild.name)
                              ,description="Here's what I've gathered about the server")
        server_embed.set_author(name="An Author")
        server_embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
        server_embed.add_field(name="Roles", value=str(len(ctx.guild.roles)), inline=True)
        server_embed.add_field(name="Memebers", value=str(len(ctx.guild.members)), inline=True)
        server_embed.add_field(name="Created on", value=ctx.message.guild.created_at, inline=True)
        server_embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.message.channel.send(embed=server_embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))