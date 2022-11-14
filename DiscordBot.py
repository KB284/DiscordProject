import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()


token = 'MTA0MTQ3NjU1NDE3NTI5OTU4NA.GA3WmI.LDYA1kwsF5dHV1vAmrygcQo4VwHroK0vxNPts4'

intent = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intent)
client = discord.Bot()

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "joke":
            jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                     "Why is she called llene? She\
                     stands on equal legs.",
                     "What do you call a gazelle in a \
                     lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))



client.run(token)

