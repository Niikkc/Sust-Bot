import discord
import random
import linecache

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

client = discord.Client(intents=intents)
keyFile = open("key.txt", "r", encoding='utf-8')
key = keyFile.read()
print(f"KeyFile read : {key}")
keyFile.close()
companies = {}


@bot.event
async def on_ready():

    print(f'We have logged in as {bot.user}')
    file = open("companyList.txt", "r", encoding='utf-8')
    s = file.readline()

    while s != "":
        spaceIndex = s.find(" ")
        companyName = s[:spaceIndex]
        s = s[spaceIndex:]
        spaceIndex = s.find(" ")
        companyRating = s[:spaceIndex + 2]
        s = s[spaceIndex:]
        companies.update({companyName: [companyRating, []]})
        while s.find("(") != -1:
            startIndex = s.find("(")
            endIndex = s.find(")")
            ((companies.get(companyName))[1]).append(
                s[startIndex + 1: endIndex])
            s = s[endIndex:]
        s = file.readline()
    file.close()


# Grab User Input and then Look it up against the company Name
@bot.command()
async def Company_Check(ctx, *, arg):
    companyName = arg
    companyName.replace(" ", "_")
    if (companies.get(companyName) != None):
        companyRating = companies.get(companyName)[0]
        colorCode = 0x00ff00
        if int(companyRating) < 7:
            colorCode = 0xFEFF7D
        if int(companyRating) < 5:
            colorCode = 0xFF8000
        if int(companyRating) < 2:
            colorCode = 0xFF0000
        embedVar = discord.Embed(
            title=companyName, description="Environmental Rating : " + str(companyRating), color=colorCode)
        embedVar.add_field(name="Fun Fact", value=str(
            (companies.get(companyName)[1])[0]), inline=False)
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(
            title="Company Not Found", color=0xFF0000)
        await ctx.send(embed=embedVar)


@bot.command()
async def Company_check(ctx, *, arg):
    companyName = arg
    companyName.replace(" ", "_")
    if (companies.get(companyName) != None):
        companyRating = companies.get(companyName)[0]
        colorCode = 0x00ff00
        if int(companyRating) < 7:
            colorCode = 0xFEFF7D
        if int(companyRating) < 5:
            colorCode = 0xFF8000
        if int(companyRating) < 2:
            colorCode = 0xFF0000
        embedVar = discord.Embed(
            title=companyName, description="Environmental Rating : " + str(companyRating), color=colorCode)
        embedVar.add_field(name="Fun Fact", value=str(
            (companies.get(companyName)[1])[0]), inline=False)
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(
            title="Company Not Found", color=0xFF0000)
        await ctx.send(embed=embedVar)


@bot.command()
async def company_check(ctx, *, arg):
    companyName = arg
    companyName.replace(" ", "_")
    if (companies.get(companyName) != None):
        companyRating = companies.get(companyName)[0]
        colorCode = 0x00ff00
        if int(companyRating) < 7:
            colorCode = 0xFEFF7D
        if int(companyRating) < 5:
            colorCode = 0xFF8000
        if int(companyRating) < 2:
            colorCode = 0xFF0000
        embedVar = discord.Embed(
            title=companyName, description="Environmental Rating : " + str(companyRating), color=colorCode)
        embedVar.add_field(name="Fun Fact", value=str(
            (companies.get(companyName)[1])[0]), inline=False)
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(
            title="Company Not Found", color=0xFF0000)
        await ctx.send(embed=embedVar)


@bot.command()
async def tip(ctx):
    tipFile = open("sustainabilityTips.txt", "r", encoding='utf-8')
    n = random.randint(0, 43)
    content = tipFile.readlines()
    await ctx.send(content[n])
    tipFile.close()

bot.run(key)
