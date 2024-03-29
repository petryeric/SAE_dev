import pygtail
import asyncio"
import discord

token = "
channel_id = 1100162737100836947  # Remove quotes to use an integer ID
log_file = "/home/eric/minecraft/logs/latest.log"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_logs():
    channel = client.get_channel(channel_id)
    while True:
        try:
            lines = pygtail.Pygtail(log_file)
            for line in lines:
                await channel.send(line)
        except FileNotFoundError:
            pass
        await asyncio.sleep(1)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await send_logs()

client.run(token)
