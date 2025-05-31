import discord
from discord.ext import commands

# インテント
intents = discord.Intents.default()
intents.message_content = True

# プレフィックス
bot = commands.Bot(command_prefix="!", intents=intents)

# 辞書
server_states = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# onコマンド
@bot.command()
async def on(ctx):
    server_states[ctx.guild.id] = True
    await ctx.send("botがonになりました")

# offコマンド
@bot.command()
async def off(ctx):
    server_states[ctx.guild.id] = False
    await ctx.send("botがoffになりました")

# 受信処理
@bot.event
async def on_message(message):
    # 自分自身の発言かdmなら無視
    if message.author == bot.user or message.guild is None:
        return

    # 確認
    is_on = server_states.get(message.guild.id, False)

    if is_on and message.content:
        await message.channel.send(f"{message.author.mention} 追記するメッセージ")

    # コマンド処理
    await bot.process_commands(message)

# 実行
bot.run("")