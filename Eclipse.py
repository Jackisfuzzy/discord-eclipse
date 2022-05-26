import discord
from discord.ext import commands
import time
import random
import math

client=commands.Bot(command_prefix='$')
client.remove_command('help')

@client.event
async def on_ready():
    game = discord.Game("$help")
    await client.change_presence(status=discord.Status.online, activity=game, afk=False)
    print('Eclipse is ready!')  

@client.command()
async def test(ctx):
    await ctx.send('Test Complete')

@client.command()
async def ping(ctx):
    await ctx.send('Client latency is {0}'.format(round(client.latency, 1)) + ' ms')

@client.command()
async def rps(ctx, input):

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
        gameresult == "I win!"
    elif playerchoice != "rock" or "paper" or "scissors":
        await ctx.send("That is an invalid choice!")
        return
    else:
        gameresult = "You win!"
    
    #Make an embed because embeds look nice
    embed = discord.Embed(title="Rock, Paper, Scissors Game", colour=discord.Colour.blurple())
    embed.add_field(name=gameresult, value="You chose `" + playerchoice + "` and I chose `" + botchoice + "`")
    embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)

    await ctx.send(embed=embed)
    
    
    
    
    #elif botchoice_str == "rock" and playerchoice == "paper":
    #    gameresult = "You win!"
    #elif botchoice_str == "rock" and playerchoice == "scissors":
    #    gameresult = "I win!"
    #elif botchoice_str == "paper" and playerchoice == "rock":
    #    gameresult = "I win!"
    #elif botchoice_str == "paper" and playerchoice == "scissors":
    #    gameresult = "You win!"
    #elif botchoice_str == "scissors" and playerchoice == "rock":
    #    gameresult = "You win!"
    #elif botchoice_str == "scissors" and playerchoice == "paper":
    #    gameresult = "I win!"
        

@client.command()
async def help(ctx):
    author = ctx.message.author    
    #Yeah this could be done better but im at my wits end here
    gamespage = discord.Embed(title="Games", colour=discord.Colour.teal())
    gamespage.add_field(name="$rps [str]", value="Play a game of rock, paper, scissors!")
    gamespage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await author.send(embed=gamespage)

    utilitypage = discord.Embed(title="Utility", colour=discord.Colour.blurple())
    utilitypage.add_field(name="$ping", value="Gives the latency between you and the bot command in miliseconds.")
    utilitypage.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await author.send(embed=utilitypage)
    
@client.command()
async def purge(ctx, *, number:int = None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send('You must input a number')
            else:
                deleted = await ctx.message.channel.purge(limit = number)
                await ctx.send(f'Messages purged by {ctx.message.author.mention}: `{len(deleted)}`')
        except:
            await ctx.send("I can't purge messages here.")
    else:
        await ctx.send('You do not have permissions to use this command.')

#Inside joke with friends.
@client.command()
async def amigay(ctx):
    userid = ctx.author.id
    userid_calc = math.sqrt(userid) / 50000000 + 7 * 1.2
    userid_calc = round(userid_calc, 1)
    await ctx.send(f'{ctx.author.mention} you are ' + str(userid_calc) + ' percent gay.')



client.run('NDg1MDU3OTYxMzU4NTI0NDI3.GLsm9B.Dgx9iqqLCIGWupr6bSRKF0OBjOgR8A5Ecp5LbI')

