import os
import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    print("noenvtoken")
    exit(1)
else:
    print(f"token accepted: {bool(TOKEN)}")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.tree.command(name="macan", description="макан")
async def macan(interaction: discord.Interaction):
    await interaction.response.send_message("xy3sos")

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(f"sync error: {e}")
    print(f"{bot.user} started")
    
app = Flask("")

@app.route("/")
def home():
    return "Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run).start()

bot.run(TOKEN)


