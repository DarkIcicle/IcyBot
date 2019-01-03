import discord


def no_connection():
    no_con = discord.Embed(title="Database Connection Error",
                           description="Unable to establish connection to the database, please try again later!",
                           color=discord.Color(0).red())
    return no_con


def no_permissions():
    no_perms = discord.Embed(title="Insufficient permissions",
                             description="Sorry, you cannot do that!",
                             color=discord.Color(0).red())
    return no_perms
