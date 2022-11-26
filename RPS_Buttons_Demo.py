import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is online")


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # Rock
    @discord.ui.button(label="Who are you?.", style=discord.ButtonStyle.blurple)
    async def Bot_Identify(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("I am a bot.")

    # Paper
    @discord.ui.button(label="What is your purpose?", style=discord.ButtonStyle.blurple)
    async def Bot_Purpose(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="To react to buttons.")


    # Scissors
    @discord.ui.button(label="Why is there so many buttons?", style=discord.ButtonStyle.blurple)
    async def Bots_Hubris(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="Because I have the power to make many!!")


    @discord.ui.button(label="Quit", style=discord.ButtonStyle.red)
    async def Quit(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=f"Goodbye kid")
        embed.add_field(name="Bye Bye", value="Turning off button functionality.")
        await interaction.response.edit_message(embed=embed)
        self.value = False
        self.stop()


@bot.command()
async def menu(ctx):
    view = Menu()
    view.add_item(discord.ui.Button(label="Tired of studying?", style=discord.ButtonStyle.link,
                                    url="https://youtu.be/M3Keg5XKJO8"))
    view.add_item(discord.ui.Button(label="Github Link", style=discord.ButtonStyle.link,
                                    url="https://github.com/KB284"))
    view.add_item(discord.ui.Button(label="NileRed is a cool chemist.", style=discord.ButtonStyle.link,
                                    url="https://www.youtube.com/watch?v=saANxD0cqy0"))

    await ctx.reply("Click to know about me...", view=view)


bot.run("MTA0MTQ3NjU1NDE3NTI5OTU4NA.GBGYAJ.1f7I5HnYILJdSzNmyCC76w4AxdIjRDHQj0gpvw")
