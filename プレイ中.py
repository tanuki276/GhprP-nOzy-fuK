import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログイン成功：{bot.user}")
    activity = discord.Game(name="ここ")
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run("")