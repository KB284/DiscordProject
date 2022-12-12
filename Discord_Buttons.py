import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client= discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is online")


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="What is the project?.", style=discord.ButtonStyle.blurple)
    async def Project_Info(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("The purpose of the project was to make me a bot that can play "
                                                "rock, paper, scissors.")

    @discord.ui.button(label="How do I play?", style=discord.ButtonStyle.blurple)
    async def Instruction(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="You simply type '!rps' and then type your weapon of choice.")


    @discord.ui.button(label="What else can you do", style=discord.ButtonStyle.blurple)
    async def Additional_Info(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="I can direct you to the embedded links.")


    @discord.ui.button(label="Quit", style=discord.ButtonStyle.red)
    async def Quit(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=f"You're done?")
        embed.add_field(name="Bye Bye", value="See you next time.")
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
    await ctx.reply("Lets Play!", view=view)


bot.run("MTA0MTQ3NjU1NDE3NTI5OTU4NA.GBGYAJ.1f7I5HnYILJdSzNmyCC76w4AxdIjRDHQj0gpvw")
