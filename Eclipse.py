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

 #Word trigger commands---------
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
    choices = ["It was. https://cdn.discordapp.com/attachments/965019294821928980/981766174247358554/download_5.jpeg", 
    "It wasn't. https://cdn.discordapp.com/attachments/965019294821928980/981766174536790106/images_7.jpeg", 
    "Maybe? https://cdn.discordapp.com/attachments/965019294821928980/981766175111389224/download_4.jpeg"
    ]
    choice = random.choice(choices)
    return choice

 #Help Menu-------------------------------------------
@client.command()
async def help(ctx, Optional:str=None):
    if Optional == None:
        helpmenu = discord.Embed(title="Help Menu", colour=discord.Colour.red(), inline=False)
        helpmenu.add_field(name="Games", value="Various games you can play with Eclipse", inline=False)
        helpmenu.add_field(name="Utility", value="Tweak and change the bot", inline=False)
        helpmenu.add_field(name="Moderation", value="Commands that will help moderators keep the peace", inline=False)
        helpmenu.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.reply(embed=helpmenu, mention_author=False)
    
    elif Optional == str.lower("games"):
        gamespage = discord.Embed(title="Games", colour=discord.Colour.teal(), inline=False)
        gamespage.add_field(name="$rps [str]", value="Play a game of rock, paper, scissors!", inline=False)
        gamespage.add_field(name="$rtd [int]", value="Rolls a random dice between 0 and [int]!", inline=False)
        gamespage.add_field(name="$spacefact", value="Sends a random spacefact!", inline=False)
        gamespage.add_field(name="$8ball", value="Use the magical 8b ball to tell you your future!", inline=False)
        gamespage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.reply(embed=gamespage, mention_author=False)
    
    elif Optional == str.lower("utility"):
        utilitypage = discord.Embed(title="Utility", colour=discord.Colour.blurple(), inline=False)
        utilitypage.add_field(name="$ping", value="Gives the latency between you and the bot command in miliseconds.", inline=False)
        utilitypage.add_field(name="$createrole [name] [r] [g] [b]", value="Creates a role based on the user's input, all fields seperated by spaces", inline=False)
        utilitypage.add_field(name="$getavatar [user]", value="Retrieves a user's avatar.", inline=False)
        utilitypage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.reply(embed=utilitypage, mention_author=False)
    
    elif Optional == str.lower("moderation"):
        moderationpage = discord.Embed(title="Moderation", colour=discord.Colour.blue(), inline=False)
        moderationpage.add_field(name="$purge [int]", value="Deletes [int] amount of messages", inline=False)
        moderationpage.add_field(name="$ban [user] [reason]", value="Ban a user", inline=False)
        moderationpage.add_field(name="$kick [user] [reason]", value="Kick a user", inline=False)
        moderationpage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.reply(embed=moderationpage, mention_author=False)
    

 #Moderation commands-----------------------
@client.command()
async def purge(ctx, *, number:int = None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.reply('You must input a number', mention_author=False)
            else:
                deleted = await ctx.message.channel.purge(limit = number + 1)
                await ctx.reply(f'Messages purged by {ctx.message.author.mention}: `{len(deleted) - 1}`', mention_author=False)
                sleep(2)
                await ctx.message.channel.purge(limit=1)
        except:
            await ctx.reply("I can't purge messages here.", mention_author=False)
    else:
        await ctx.reply('You do not have permissions to use this command.', mention_author=False)

@client.command()
async def ban(ctx, user : discord.Member, *, reason = None):
    if ctx.message.author.guild_permissions.ban_members:
        if user is None:
            await ctx.reply('You must input a User.', mention_author=False)
        else:
            await user.ban(reason = reason)
            await ctx.reply(f"{user} has been banned for the reason: '{reason}'", mention_author=False)
    else:
        await ctx.reply("You do not have permission to use this command.", mention_author=False)

@client.command()
async def kick(ctx, user : discord.Member, *, reason = None):
    if ctx.message.author.guild_permissions.kick_members:
        if user is None:
            await ctx.reply("You must input a User.", mention_author=False)
        else:
            await user.kick(reason = reason)
            await ctx.reply(f"{user} has been kicked for the reason: '{reason}'", mention_author=False)
    else:
        await ctx.reply("You do not have permission to use this command.", mention_author=False)

 #Utility commands------------------------------        
@client.command()
async def createrole(ctx, name, r, g, b):
    guild = ctx.guild
    colour= discord.Color.from_rgb(int(r), int(g), int(b))
    await guild.create_role(name=name, color=colour)
    await ctx.reply(f"The role `{name}` has been created", mention_author=False)

@client.command()
async def ping(ctx):
    await ctx.reply('Client latency is {0}'.format(round(client.latency, 1)) + ' ms', mention_author=False)

@client.command()
async def getavatar(ctx, user: discord.Member):
    gavembed = discord.Embed(title=f"{user}'s avatar", colour=discord.Colour.dark_gold(), inline=False)
    gavembed.set_image(url=user.avatar_url)
    await ctx.reply(embed=gavembed, mention_author=False)

 #Fun commands (Games, etc)------------------------------------------------------
@client.command(name="8ball")
async def _8ball(ctx):
    pos_choices=["It is certian", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
    neu_choices=["Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
    neg_choices=["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    #Postive and Negative choices have a 40% chance of occuring while the indecisive answers to only have a 10% chance of occuring.
    choice = random.randint(0,100)
    if choice < 45:
        reply_choice = random.choice(pos_choices)
    elif choice > 55:
        reply_choice = random.choice(neg_choices)
    elif choice > 45 and choice < 55:
        reply_choice = random.choice(neu_choices)
    else:
        reply_choice = "Saturn fucking sucks a programming"
    
    embed = discord.Embed(title="Magic 8 ball", color=discord.Colour.blurple())
    embed.add_field(name="Reading your future...", value=':8ball:')
    embed.set_image(url="https://cdn.discordapp.com/attachments/430729014924148746/981776201481879673/PngItem_2581937.png")
    embed1 = await ctx.reply(embed=embed, mention_author=False)
    sleep(4)
    embed2 = discord.Embed(title=reply_choice, colour=discord.Colour.greyple())
    await embed1.edit(embed=embed2)

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
        await ctx.reply("Invalid Choice :x:", mention_author=False)
        return
    
    else:
        gameresult = "You win!"

        
    #Make an embed because embeds look nice
    embed = discord.Embed(title="Rock, Paper, Scissors Game", colour=discord.Colour.blurple())
    embed.add_field(name=gameresult, value="You chose `" + playerchoice + "` and I chose `" + botchoice + "`")
    embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)

    await ctx.reply(embed=embed, mention_author=False)

#Inside joke with friends.
@client.command()
async def amigay(ctx):
    userid = ctx.author.id
    userid_calc = math.sqrt(userid) / 50000000 + 7 * 1.2
    userid_calc = round(userid_calc, 1)
    await ctx.reply(f'{ctx.author.mention} you are ' + str(userid_calc) + ' percent gay.', mention_author=False)

@client.command()
async def rtd(ctx, amount: int):
    roll_amt = random.randint(0, amount)
    msg1em = discord.Embed(title="Rolling the dice..", color=discord.Colour.green())
    msg1em.set_image(url="https://cdn.discordapp.com/attachments/485068054795911169/979603428303048734/diceroll1.gif")
    embed1 = await ctx.reply(embed=msg1em, mention_author=False)
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
    await ctx.reply(mylines[factchoice], mention_author=False)

client.run('')

