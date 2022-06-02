import discord
from discord.ext import commands
import time
import random
import math
from typing import Optional
from time import sleep

client=commands.Bot(command_prefix='$', help_command = None)

@client.event
async def on_ready():
    game = discord.Game("$help")
    await client.change_presence(status=discord.Status.online, activity=game, afk=False)
    print('Eclipse is ready!')  

@client.event
async def on_message(message):
    #ben found this funny?
    if "peter" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/965019294821928980/981762908344176660/images_6.jpeg")
    
    elif "phil" in message.content.lower():
        await message.channel.send("Is it?")
        sleep(3)
        await message.channel.send(is_it())
    
    else:
        await client.process_commands(message)

def is_it():
    choices = ["It was. https://cdn.discordapp.com/attachments/965019294821928980/981766174247358554/download_5.jpeg", "It wasn't. https://cdn.discordapp.com/attachments/965019294821928980/981766174536790106/images_7.jpeg", "Maybe? https://cdn.discordapp.com/attachments/965019294821928980/981766175111389224/download_4.jpeg"]
    choice = random.choice(choices)
    return choice

@client.command()
async def test(ctx):
    await ctx.send('Test Complete')

@client.command(name="8ball")
async def _8ball(ctx):
    pos_choices=["It is certian", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
    neu_choices=["Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
    neg_choices=["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    
    choice = random.randint(0,1)
    if choice == 0:
        reply_choice = random.choice(pos_choices)
    elif choice == 1:
        reply_choice = random.choice(neg_choices)
    else:
        reply_choice = random.choice(neu_choices)
    
    embed = discord.Embed(title="Magic 8 ball", color=discord.Colour.blurple())
    embed.add_field(name="Reading your future...", value=':8ball:')
    embed.set_image(url="https://cdn.discordapp.com/attachments/430729014924148746/981776201481879673/PngItem_2581937.png")
    embed1 = await ctx.send(embed=embed)
    sleep(4)
    embed2 = discord.Embed(title=reply_choice, colour=discord.Colour.greyple())
    await embed1.edit(embed=embed2)


@client.command()
async def ping(ctx):
    await ctx.send('Client latency is {0}'.format(round(client.latency, 1)) + ' ms')

@client.command()
async def rps(ctx, input: str):

    playerchoice = str.lower(input)
    
    choices = ["rock", "paper", "scissors"]
    
    botchoice = random.choice(choices)
   
    #Kill me
    if botchoice == playerchoice:
        gameresult = "It's a tie!"
    
    elif botchoice == "rock" and playerchoice == "scissors":
        gameresult = "I win!"
    
    elif botchoice == "paper" and playerchoice == "rock":
        gameresult = "I win!"
    
    elif botchoice == "scissors" and playerchoice == "paper":
        gameresult = "I win!"
    
    elif playerchoice not in choices:
        await ctx.send("Invalid Choice :x:")
        return
    
    else:
        gameresult = "You win!"

        
    #Make an embed because embeds look nice
    embed = discord.Embed(title="Rock, Paper, Scissors Game", colour=discord.Colour.blurple())
    embed.add_field(name=gameresult, value="You chose `" + playerchoice + "` and I chose `" + botchoice + "`")
    embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)

    await ctx.send(embed=embed)

@client.command()
async def help(ctx, Optional:str=None):
    if Optional == None:
        helpmenu = discord.Embed(title="Help Menu", colour=discord.Colour.red(), inline=False)
        helpmenu.add_field(name="Games", value="Various games you can play with Eclipse", inline=False)
        helpmenu.add_field(name="Utility", value="Tweak and change the bot", inline=False)
        helpmenu.add_field(name="Moderation", value="Commands that will help moderators keep the peace", inline=False)
        helpmenu.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=helpmenu)
    
    elif Optional == str.lower("games"):
        gamespage = discord.Embed(title="Games", colour=discord.Colour.teal(), inline=False)
        gamespage.add_field(name="$rps [str]", value="Play a game of rock, paper, scissors!", inline=False)
        gamespage.add_field(name="$rtd [int]", value="Rolls a random dice between 0 and [int]!", inline=False)
        gamespage.add_field(name="$spacefact", value="Sends a random spacefact!", inline=False)
        gamespage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=gamespage)
    
    elif Optional == str.lower("utility"):
        utilitypage = discord.Embed(title="Utility", colour=discord.Colour.blurple(), inline=False)
        utilitypage.add_field(name="$ping", value="Gives the latency between you and the bot command in miliseconds.", inline=False)
        utilitypage.add_field(name="$createrole [name] [r] [g] [b]", value="Creates a role based on the user's input, all fields seperated by spaces", inline=False)
        utilitypage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=utilitypage)
    
    elif Optional == str.lower("moderation"):
        moderationpage = discord.Embed(title="Moderation", colour=discord.Colour.blue(), inline=False)
        moderationpage.add_field(name="$purge [int]", value="Deletes [int] amount of messages", inline=False)
        moderationpage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=moderationpage)
    
@client.command()
async def purge(ctx, *, number:int = None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send('You must input a number')
            else:
                deleted = await ctx.message.channel.purge(limit = number + 1)
                await ctx.send(f'Messages purged by {ctx.message.author.mention}: `{len(deleted) - 1}`')
                sleep(2)
                await ctx.message.channel.purge(limit=1)
        except:
            await ctx.send("I can't purge messages here.")
    else:
        await ctx.send('You do not have permissions to use this command.')
        
@client.command()
async def createrole(ctx, name, r, g, b):
    guild = ctx.guild
    colour= discord.Color.from_rgb(int(r), int(g), int(b))
    await guild.create_role(name=name, color=colour)
    await ctx.send(f"The role `{name}` has been created")

#Inside joke with friends.
@client.command()
async def amigay(ctx):
    userid = ctx.author.id
    userid_calc = math.sqrt(userid) / 50000000 + 7 * 1.2
    userid_calc = round(userid_calc, 1)
    await ctx.send(f'{ctx.author.mention} you are ' + str(userid_calc) + ' percent gay.')

@client.command()
async def rtd(ctx, amount: int):
    roll_amt = random.randint(0, amount)
    msg1em = discord.Embed(title="Rolling the dice..", color=discord.Colour.green())
    msg1em.set_image(url="https://cdn.discordapp.com/attachments/485068054795911169/979603428303048734/diceroll1.gif")
    embed1 = await ctx.send(embed=msg1em)
    sleep(3)
    msg2em = discord.Embed(title="You rolled a...", color=discord.Colour.green())
    msg2em.add_field(name=str(roll_amt), value="\u200b")
    msg2em.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await embed1.edit(embed=msg2em)

@client.command()
async def spacefact(ctx):
    factchoice = random.randint(1, 9)
    mylines = []
    with open(r'C:\Users\Eric\Desktop\spacefacts.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    await ctx.send(mylines[factchoice])


#TODO find how to pass USERID through discord.User.avatar_url
@client.command()
async def getavatar(ctx, uid: int):
    gavembed = discord.Embed(title='User\'s Avatar', colour=discord.Colour.dark_gold(), inline=False)
    gavembed.set_image(uid.discord.User.avatar_url)
    await ctx.send(embed=gavembed)

client.run('')

