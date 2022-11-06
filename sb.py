import discord
import random
import linecache

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')
# bot = commands.Bot(intents=discord.Intents.default(),command_prefix='$')

client = discord.Client(intents=intents)
keyFile = open("key.txt", "r", encoding='utf-8')
key = keyFile.read()
print(f"KeyFile read : {key}")
keyFile.close()
companies = {}


@bot.event
async def on_ready():

    print(f'We have logged in as {bot.user}')
    # await client.change_presence(activity=discord.Game(name='with trees'))

    file = open("companyList.txt", "r", encoding='utf-8')
    s = file.readline()

    # print(s)

    while s != "":
        # print("asdlfjasldf")
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

    # print(companies)
    file.close()


# Grad User Input and then Look it up against the company Name
@bot.command()
# @client.command()
async def Company_Check(ctx, *, arg):
    # print(companies)
    companyName = arg
    companyName.replace(" ", "_")
    print(companyName)
    companyRating = companies.get(companyName)[0]
    print(companyRating)
    colorCode = 0x00ff00
    if int(companyRating) < 7:
        colorCode = 0xFEFF7D
    if int(companyRating) < 5:
        colorCode = 0xFF8000
    if int(companyRating) < 2:
        colorCode = 0xFF0000

        #colorCode = 0xFF0000

    embedVar = discord.Embed(
        title=companyName, description="Environmental Rating : " + str(companyRating), color=colorCode)
    embedVar.add_field(name="Fun Fact", value=str(
        (companies.get(companyName)[1])[0]), inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def tip(ctx):
    tipFile = open("sustainabilityTips.txt", "r", encoding='utf-8')
    n = random.randint(0, 9)
    content = tipFile.readlines()
    await ctx.send(content[n])
    tipFile.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #companyList = {str : [start,end]}
    if message.content.startswith('Sustainability Bot where at?'):
        await message.channel.send('Hello!')

    # if message.content.startswith('test'):
    #     #companyName = "Shein" #TODO input
    #     companyName = input()
    #     companyRating = companies.get(companyName)[0]
    #     colorCode = 0x00ff00
    #     if int(companyRating) < 7:
    #         colorCode = 0xFEFF7D
    #     if int(companyRating) < 5:
    #         colorCode = 0xFF8000
    #     if int(companyRating) < 2:
    #         colorCode = 0xFF0000

    #     #colorCode = 0xFF0000

    #     embedVar = discord.Embed(title= companyName, description="Environmental Rating : " + str(companyRating), color=colorCode)
    #     embedVar.add_field(name="Fun Fact", value=str((companies.get(companyName)[1])[0]), inline=False)
    #     await message.channel.send(embed=embedVar)


#     elif message.content.startswith('tip'):
# <<<<<<< HEAD
#         # await message.channel.send("test")
#         tipFile = open("sustainabilityTips.txt", "a")
# =======
#         #await message.channel.send("test")
#         tipFile = open("sustainabilityTips.txt","r", encoding='utf-8')
# >>>>>>> 5cd0480a12e30c5ecc371b88205b4c5b39cc5943
#         n = random.randint(0, 9)
#         content = tipFile.readlines()
#         #await message.channel.send(n)
#         await message.channel.send(content[n])
#         tipFile.close()

bot.run(key)
# client.run("MTAzODUxNTg4MDY1MDM1ODgxNA.Go8sWi.mHh1Jj8Xyti11P4f0yIF_CrzE_yhfc-t3vynHg")


# Bot command to take in an arg
# @bot.command()
# async def CompanyCheck(ctx, arg):
#     await ctx.send(arg)
