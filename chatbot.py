import discord
import requests
import json

# キーととーくん
DISCORD_TOKEN = ""
GENAI_API_KEY = ""

# geminiapiのエンドポイント (v1beta & generateContent)
GENAI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={GENAI_API_KEY}"

# Discordクライアント作成
intents = discord.Intents.default()
intents.message_content = True  # インテント
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログイン成功: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = str(message.content).strip()
    print(f"受信メッセージ: {content}")

    if content.startswith("!ai "):
        prompt = content[4:].strip()
        print(f"プロンプト: {prompt}")

        try:
            # geminiapiにリクエストを送信
            headers = {
                "Content-Type": "application/json"
            }
            data = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }

            # request
            response = requests.post(GENAI_API_URL, headers=headers, json=data)
            
            if response.status_code == 200:
                response_data = response.json()
                generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
                await message.channel.send(generated_text)
            else:
                print(f"エラー発生: {response.status_code} {response.text}")
                await message.channel.send("エラーが発生しました。")

        except Exception as e:
            print(f"エラー発生: {str(e)}")
            await message.channel.send("エラーが発生しました。")

# 機動
client.run(DISCORD_TOKEN)