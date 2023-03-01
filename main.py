import discord
from discord.ext import commands
from time import sleep
import asyncio

token = ""
intents = discord.Intents.all()
block_words = ["nigger", "nigga", "http://", "https://", "discord.gg/", "wanker"]
bot = commands.Bot(command_prefix='?', help_command=None, intents=intents)


@bot.command()
async def boosts(ctx):
    await ctx.reply(ctx.guild.premium_subscription_count)
    print("boosts command used")

@bot.command()
async def purge(ctx, amount):
    await ctx.channel.purge(limit=int(amount))
    print("purged command used")

@bot.command()
async def fun(ctx):
  message = await ctx.send("8===D")
  await asyncio.sleep(0.5)
  await message.edit(content="8==👊D")
  await asyncio.sleep(0.5)
  await message.edit(content="8=👊=D")
  await asyncio.sleep(0.5)
  await message.edit(content="8==👊D")
  await asyncio.sleep(0.5)
  await message.edit(content="8=👊=D💦")

@bot.command()
async def inv(ctx):
    message = await ctx.send("Join discord.gg/spoof it is the best!")
    message = await ctx.send("https://cdn.discordapp.com/attachments/1054386904667267114/1054387701719240714/standard_3.gif")
    print("invite was used")

@bot.command()
async def service(ctx):
    embed=discord.Embed(title="Our services", url="https://rar.codes/", description="This is all the information right now about what we will be doing in the furture", color=0x109319)
    embed.set_author(name="RARcodes", url="https://www.youtube.com/@RARcodes", icon_url="https://yt3.googleusercontent.com/o2uTWNDs4B8ExTwMoEe-y-zcSiMMowcKAqIS6-fRXcmQERl_jOOxxkfZZMVZW2MI21hA4jekFA=s88-c-k-c0x00ffffff-no-rj")

    embed.add_field(name="Tiktok tools", value="Our tiktok tools are comming out very soon! we have a couple avalible. but you will need to message the Owner or an Admin.", inline=False)
    embed.add_field(name="Twitch tools", value="This should be coming out quite soon. Our tools we will offe will be viewer bots. Follow bots and probably more!", inline=True)
    embed.add_field(name="Game cheats", value="We will most likely have some game cheats. Like Minecraft, Valorant, fortnite, and a whole bunch more.", inline=True)

    embed.set_footer(text="This will all be coming soon. some before the other.")
    ## User's display name in the server
    ctx.author.display_name
    ctx.author.avatar_url
    await ctx.send(embed=embed)

@bot.command()
async def help1(ctx):
    embed = discord.Embed(title="Commands list", description="Here are the available commands:", color=0x01fd1a)
    embed.add_field(name="?help", value="This command with give you our help screen", inline=False)
    embed.add_field(name="?boosts", value="This will show you how many boosts our server is on", inline=False)
    embed.add_field(name="?inv", value="this will send the advert to our server", inline=False)
    embed.add_field(name="?fun", value="this will send a fun message 😏", inline=False)
    await ctx.send(embed=embed)

title = "Commands list"
description = "**• ?help** `This command with give you our help screen`\n\n**• ?boosts** `This will show you how many boosts our server is on`\n\n**• ?inv** `this will send the advert to our server `\n\n**• ?fun** `this will send a fun message 😏`"

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=title, description=description, color=0x01fd1a)
    await ctx.send(embed=embed)

    
print("OGI IS ONLINE")
bot.run(token) #tukz is black



