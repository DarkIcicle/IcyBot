import discord


class EmbedBuilder:
    embed = None

    def __init__(self):
        self.embed = discord.Embed(colour=discord.Colour.red())

    def no_connection(self):
        self.embed.title = "Database Connection Error"
        self.embed.description = "Unable to establish connection to the database, please try again later!"
        return self.embed

    def no_permissions(self):
        self.embed.title = "Insufficient permissions"
        self.embed.description = "Sorry, you cannot do that!"
        return self.embed

    def custom(self, title, description):
        self.embed.title = title
        self.embed.description = description
        return self.embed

