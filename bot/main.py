import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.tree.command(name="build")
async def build(interaction:discord.Interaction):
    cwd = os.getcwd()
    os.chdir(cwd + "\file")
    await interaction.response.send_message("Building in progress...")
    os.system("gradlew build")
    for file in os.listdir("build\libs"):
        if file.endswith("-sources.jar"):
            continue
        with open(f"build/libs/{file}", "rb") as f:
            await interaction.channel.send(file=discord.File(f, filename="CoflMod-1.4.3"))
    await interaction.edit_original_response(content="Build complete!")
bot.run("MTA5MzQxMjcxNTgzNTQzNzA3Nw.GrZ-PW.o-2MmqQzvjFxk9LdXv-dPYN8wXBZ7jJzQ-KGyw")