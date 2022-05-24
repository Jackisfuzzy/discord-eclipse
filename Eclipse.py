import discord
from discord.ext import commands

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

client.run('NDg1MDU3OTYxMzU4NTI0NDI3.GLsm9B.Dgx9iqqLCIGWupr6bSRKF0OBjOgR8A5Ecp5LbI')