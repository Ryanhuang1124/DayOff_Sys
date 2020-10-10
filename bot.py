import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '!')

bot.run("NzY0NTQyMjQ4NzU0NzQxMjU4.X4HxdA.4nvG_vmVlf8ZR5_5o4FbNG38DZk")

@bot.event
async def on_ready():
    print(">>Bot is online")

# @bot.event
# async def on_menber_join(member):
#     channel = bot.get_channel(764548549257199726)
#     print(member)
#     await channel.send(f'{member}')

