# __main__.py
import discord,os
from os.path import join, dirname
from dotenv import load_dotenv

import create_img
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("DISCORD_TOKEN")
APPLICATION_ID = os.environ.get("APPLICATION_ID")

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f"Ready: {client.user}")

@client.event
async def on_message(message:discord.Message):
    if message.author.bot:return
    if f"<@{APPLICATION_ID}>" in message.content:
        text = message.content.replace(f"<@{APPLICATION_ID}> ","").replace(f"<@{APPLICATION_ID}>","").replace("...","…")
        try:
            if len(text) == 0:
                await message.reply(content=f"`@mention テキスト`で画像作れるぞ")
                return
            if create_img.image_process(base_text=f"{text}") == 0:
                await message.reply(content="",file=discord.File(f'result.png'))
            else:
                await message.reply(content="文字数減らせばいいぞ(16文字まで)")
        except discord.errors.HTTPException:
            pass
        except Exception as e:
            print(e)
if __name__ == '__main__':
    client.run(TOKEN)