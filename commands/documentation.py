import discord
from discord.ext import commands


def words_in_string(word_list, string):
    return set(word_list).intersection(string.split())


def find_line(line_array, content, cls = False):
    if cls is True:
        find_term = "class " + content.lower() + ":"
    else:
        find_term = "def " + content.lower() + "(self"
    for l_num in range(len(line_array)):
        if find_term in line_array[l_num].lower():
            return l_num
    return None


class Documentation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dpy(self,ctx):
        """"
        Basic doc retrieval, very messy at the moment and broken/incomplete

        :param ctx: The context for the trigger event
        :return: Error embed if none, otherwise the doc embed
        """
        to_find = ctx.message.content[5:].split('#')

        c_find = to_find[0].lower()
        f_find = to_find[1].replace("()", "").lower() if len(to_find) != 1 else None

        with open("discord/{}.py".format(c_find)) as file:
            c_find = c_find[0].upper() + c_find[1:]
            key_words = ["Parameters", "Attributes", "Raises", "Returns"]
            lines = file.read().splitlines()
            test = "https://discordpy.readthedocs.io/en/rewrite/api.html#discord.%s%s" % (c_find, "." + f_find if f_find else "")
            fun_line = find_line(lines, f_find) if f_find else find_line(lines, c_find, True)
            if fun_line is None:
                err_embed = discord.Embed(title="Error!", color=discord.Colour.red(), description="I could not find it!")
                return await ctx.channel.send(embed=err_embed)
            doc_embed = discord.Embed(title="{}".format(c_find + "%s"%("#" + f_find if f_find else "")), colour=discord.Colour.blue(), url=test)
            doc_embed.set_author(name="Discord.py Documentation", icon_url="https://i.imgur.com/RPrw70n.png")
            overview = ""
            for l_num in range(fun_line, len(lines)):
                if words_in_string(key_words, lines[l_num]):
                    break
                overview += lines[l_num]
            doc_embed.description = overview
            print(doc_embed.description)
        return await ctx.channel.send(embed=doc_embed)

def setup(bot):
    bot.add_cog(Documentation(bot))






