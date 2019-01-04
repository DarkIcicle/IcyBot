import asyncio
import json
import random
import os
from IcyBot.Utils.sql_connection import MySQLConnection

import discord
from discord.ext import commands
file = open("botconfig.json", 'r')
configFile = json.load(file)

bot = commands.Bot(command_prefix=configFile['prefix'])
muted_users = {}
con = MySQLConnection()

con.connect()


@bot.event
async def on_ready():
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))


@bot.event
async def on_message(message):
    chance = random.randint(1, 10)
    await bot.process_commands(message)
    if message.content.startswith('>'):
        return
    if con.connection is None:
        return
    if int(message.author.id) == 419704042604724224:
        if message.embeds is not None:
            if message.embeds[0].title == 'Coins':
                await asyncio.sleep(4.0)
                await message.delete
        return
    discord_id = message.author.id
    con.create_user(discord_id, message.author.name)
    if chance < 5:
        coins_earned = random.randint(1, 5)
        con.update_coins(discord_id, coins_earned)
        coin_embed = discord.Embed(title="Coins", description="{} has found ".format(message.author.mention) + str(coins_earned) + " coins!",
                                   color=0xFFB200)
        await message.channel.send(embed=coin_embed, delete_after=4)

    experience = random.randint(1, 15)
    current_exp = con.get_experience(discord_id)
    current_level = con.get_level(discord_id)
    experience_needed = current_level*100
    if current_exp + experience >= experience_needed:
        overflow_experience = (current_exp+experience)-experience_needed
        con.update_level(discord_id)
        con.set_experience(discord_id, overflow_experience)
        level_up = discord.Embed(title="Level Up!",
                                 description="Congrats {}, you have reached level {}".format(message.author.mention, con.get_level(discord_id)))
        await bot.send_message(message.channel, embed=level_up)
    else:
        con.update_experience(discord_id, experience)

failed = []


def load_ext(ext_name):
    try:
        bot.load_extension(f"commands.{ext_name}")
        print("Loaded " + ext_name + ".py")
        if ext_name in failed:
            failed.remove(ext_name)
    except Exception as e:
        print("Failed to load " + ext_name)
        failed.append(ext_name)
        print(e)


for file in os.listdir("commands"):
    if file.endswith(".py"):
        name = file[:-3]
        load_ext(name)

if len(failed) > 0:
    print("Attempting to load failed extensions...")
    for ext in failed:
        load_ext(ext)

bot.run(configFile['token'])
