import discord 
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

jacky = commands.Bot(command_prefix='/', intents=intents)
client = discord.Client(intents=intents)

@jacky.event
async def on_ready():
    print(f'Ready to sail!') 

@jacky.event
async def on_message(message):
    print(f'Shout from {message.author}: {message.content}')

    await jacky.process_commands(message)

@jacky.command(pass_context = True)
async def join(ctx):
    for voice_channel in ctx.guild.voice_channels:
        for member in voice_channel.members:
            if member == ctx.message.author:
                voice_state = await voice_channel.connect()

                global VChannel
                VChannel = voice_channel

                global VState
                VState = voice_state

                print(VChannel)

@jacky.command(pass_context = True)
async def leave(ctx):
    await VState.disconnect()

jacky.run(os.getenv('DISCORD_BOT_API_KEY')) 