import discord
import random

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

    print(f'We have logged in as {client.user}')
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
async def CompanyCheck(ctx, *, arg):
    print(companies)
    companyName = arg
    companyName.replace(" ", "_")
    print(companyName)
    companyRating = companies.get(companyName)[0]
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
        print("tests")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #companyList = {str : [start,end]}
    if message.content.startswith('Sustainability Bot where at?'):
        await message.channel.send('Hello!')

    # if message.content.startswith('test'):
    #     companyName = arg1 #TODO input
    #     embedVar = discord.Embed(title= companyName, description="Environmental Rating : " + str(companies.get(companyName)[0]), color=0x00ff00)
    #     embedVar.add_field(name="Fun Fact", value=str((companies.get(companyName)[1])[0]), inline=False)
    #     #embedVar.add_field(name="Field2", value="hi2", inline=False)
    #     await message.channel.send(embed=embedVar)

    # Check how good a specific company is
    elif message.content.startswith('companyCheck'):
        # await message.channel.send('hi')
        # companyList.get()
        s = message.content.split()
        if (len(s) == 1):
            await message.channel.send("Please enter company : ")
            if message[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        elif (len(s) == 2):
            if s[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        else:
            await message.channel.send('Invalid Input')

    elif message.content.startswith('tip'):
        # await message.channel.send("test")
        tipFile = open("sustainabilityTips.txt", "a")
        n = random.randint(0, 9)
        await message.channel.send(n)
        await message.channel.send(tipFile.read([n]))
        tipFile.close()

bot.run(key)
# client.run("MTAzODUxNTg4MDY1MDM1ODgxNA.Go8sWi.mHh1Jj8Xyti11P4f0yIF_CrzE_yhfc-t3vynHg")


# Bot command to take in an arg
# @bot.command()
# async def CompanyCheck(ctx, arg):
#     await ctx.send(arg)
