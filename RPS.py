import discord
import random
from discord.ext import commands
from Discord_Buttons import menu

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.command(name='rps', aliases=['RockPaperScissors'])
async def rps(ctx, user_choice, *, arg:str='None'):
    choices = ['rock','paper','scissors']
    bot_choices = random.choice(choices)
    user_choice = user_choice.lower()

    if bot_choices == user_choice:
        await ctx.send(f'This was a tie! bot of us picked {bot_choices}')
    elif bot_choices == "rock" and user_choice == "paper":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You won!')
    elif bot_choices == "rock" and user_choice == "scissors":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You lost!')

    elif bot_choices == "paper" and user_choice == "scissors":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You won!')
    elif bot_choices == "paper" and user_choice == "rock":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You lost!')

    elif bot_choices == "scissors" and user_choice == "rock":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You won!')
    elif bot_choices == "scissors" and user_choice == "paper":
        await ctx.send(f'You picked {user_choice}, I picked {bot_choices}.\nResult: You lost!')

    else:
        await ctx.send(f'Make sure your inputs are either {choices}')

client.run("MTA0MTQ3NjU1NDE3NTI5OTU4NA.GBGYAJ.1f7I5HnYILJdSzNmyCC76w4AxdIjRDHQj0gpvw")