import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # インテント
bot = commands.Bot(command_prefix="!", intents=intents)

# NGワード
ng_words = []

@bot.event
async def on_ready():
    print(f"{bot.user} ログイン成功")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # 不適切な単語を検知
    if any(ng in message.content for ng in ng_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 不適切な単語を検知しました。")
        return

    await bot.process_commands(message)

# Botトークン
bot.run("")  # Token
