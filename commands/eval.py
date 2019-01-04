import discord
from discord.ext import commands


class Eval:
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def e(self, ctx):
        if not isinstance(ctx.channel, discord.abc.GuildChannel):
            return

        try:
            to_eval = eval(ctx.message.content[3:])
        except Exception as e:
            err_embed = discord.Embed(color=discord.Colour.red(), title="Something went wrong!")
            err_embed.add_field(name="Here is the error I got", value="{}".format(e))
            return await ctx.channel.send(err_embed, delete_after=4)

        e_embed = discord.Embed(title="Evaluation",color=discord.Colour.green())
        e_embed.set_footer(text="IcyBot", icon_url=self.bot.user.avatar_url)
        e_embed.add_field(name="To evaluate", value="`{}`".format(ctx.message.content))
        e_embed.add_field(name="Evaluated", value=to_eval)
        e_embed.add_field(name="Type of", value=type(to_eval).__name__)
        return await ctx.channel.send(embed=e_embed)


def setup(bot):
    bot.add_cog(Eval(bot))
