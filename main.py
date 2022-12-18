import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='>', intents=intents)

class Buttons(discord.ui.View):  # класс описывает набор кнопок
    def __init__(self, *, timeout=180):  # конструктор класса
        super().__init__(timeout=timeout)
    # этому методу будет сопоставлена кнопка. По клику метод будет вызван.
    @discord.ui.button(label="1",style=discord.ButtonStyle.grey)
    async def gray_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        # ищи сведения об объекте discord.Interaction, чтобы понять, что ещё можно сделать в обработчике кнопки.
        await interaction.response.edit_message(content=f"This is an edited button response!")
        # альтернативно, тут ты можешь вызывать требуемые тебе методы и вообще делать что нужно

@client.command()
async def menu(ctx):  # по команде !button отсылается сообщение с кнопками
    await ctx.send(
        embed = discord.Embed(
        title="1. Короче здесь у нас шаурма\n2. На этом все",
    ),
    view=Buttons()
        )
    

client.run("MTA1MzYzODY0MzU4NTEzMDUzNg.Gq4qTi.TqsO_S8NbgV0hTaiVx5ToXZClJRHXfhVKK_4QU")
