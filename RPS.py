import discord, random
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.command()
async def rps(ctx):
    while True:

        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_choices = ["rock", "paper", "scissors"]
        computer_choices = random.choice(possible_choices)
        print(f"\nYou chose {user_action}, computer chose {computer_choices}.\n")

        if user_action not in possible_choices:
            await ctx.send("That is not a valid option, please type:"
                           " 'rock', 'paper', or 'scissors'.")
        else:
            if user_action == computer_choices:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_choices == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! You lose.")
            elif user_action == "paper":
                if computer_choices == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif user_action == "scissors":
                if computer_choices == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
rps()