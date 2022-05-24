import discord
from discord.ext import commands
import time
import random

client=commands.Bot(command_prefix='$')


@client.event
async def on_ready():
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
    botchoice = random.randint(0,2)
    
    #Because switch statements arent working
    if botchoice == 0:
        botchoice_str = "rock"
    elif botchoice == 1:
        botchoice_str = "paper"
    elif botchoice == 2:
        botchoice_str = "scissors"

    #Kill me
    if botchoice_str == playerchoice:
        gameresult = "It's a tie!"
    #Bot chooses rock, player chooses paper
    elif botchoice_str == "rock" and playerchoice == "paper":
        gameresult = "You win!"
    #Bot chooses rock, player chooses scissors
    elif botchoice_str == "rock" and playerchoice == "scissors":
        gameresult = "I win!"
    #Bot chooses paper, player chooses rock
    elif botchoice_str == "paper" and playerchoice == "rock":
        gameresult = "I win!"
    #Bot chooses paper, player chooses scissors
    elif botchoice_str == "paper" and playerchoice == "scissors":
        gameresult = "You win!"
    #Bot chooses scissors, player chooses rock
    elif botchoice_str == "scissors" and playerchoice == "rock":
        gameresult = "You win!"
    #Bot chooses scissors, player chooses paper
    elif botchoice_str == "scissors" and playerchoice == "paper":
        gameresult = "I win!"
    elif playerchoice != "rock" or "paper" or "scissors":
        await ctx.send("That is an invalid choice!")
        return
    
    #Make an embed because embeds look nice
    embed = discord.Embed(title="Rock, Paper, Scissors Game", colour=discord.Colour.blurple())
    embed.add_field(name=gameresult, value="You chose `" + playerchoice + "` and I chose `" + botchoice_str + "`")
    embed.set_footer(text=ctx.message.author)

    await ctx.send(embed=embed)

    #await ctx.send(gameresult + " You chose `" + playerchoice + "` and I chose `" + botchoice_str + "`")
    




client.run('NDg1MDU3OTYxMzU4NTI0NDI3.GLsm9B.Dgx9iqqLCIGWupr6bSRKF0OBjOgR8A5Ecp5LbI')