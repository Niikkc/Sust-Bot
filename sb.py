import discord
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=discord.Intents.default(),command_prefix='$')

client = discord.Client(intents=intents)
keyFile = open(".\Sustainability-Bot\key.txt","r")
key = keyFile.read()
print(f"KeyFile read : {key}")
keyFile.close()
companies = {}

companyList = {}

@client.event
async def on_ready():

        
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name='with trees'))

    file = open("companyList.txt", "r")
    s = file.read()
    for i in range(40):
    # while s != None:
        print("asdlfjasldf")
        spaceIndex = s.find(" ")
        companyName = s[:spaceIndex]
        s = s[spaceIndex:]
        spaceIndex = s.find(" ")
        companyRating = s[:spaceIndex]
        s = s[spaceIndex:]
        startIndex = s.find("(")
        endIndex = s.find(")")
        comment = s[startIndex : endIndex]
        print(f"Company : {companyName}, Company Rating : {companyRating}, First Comment : {comment}")
        print()

        




        s = file.read()
    file.close()
        

    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #companyList = {str : [start,end]}
    if message.content.startswith('Sustainability Bot where at?'):
        await message.channel.send('Hello!')


    #Check how good a specific company is
    elif message.content.startswith('companyCheck'):
        # await message.channel.send('hi')
        #companyList.get()
        s = message.content.split()
        if (len(s) == 1):
            await message.channel.send("Please enter company : ")
            if message[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        elif(len(s) == 2):
            if s[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        else:
            await message.channel.send('Invalid Input')

    elif message.content.startswith('tip'):
        #await message.channel.send("test")
        tipFile = open("sustainabilityTips.txt","a")
        n = random.randint(0, 9)
        await message.channel.send(n)
        await message.channel.send(tipFile.read([n]))
        tipFile.close()



#client.run(key)
client.run("MTAzODUxNTg4MDY1MDM1ODgxNA.Go8sWi.mHh1Jj8Xyti11P4f0yIF_CrzE_yhfc-t3vynHg")


#Bot command to take in an arg
# @bot.command()
# async def CompanyCheck(ctx, arg):
#     await ctx.send(arg)