import os

import discord

intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is explicitly enabled
client = discord.Client(intents=intents)


# Initialize the client with the specified intents


@client.event
async def on_ready():
  print('Logged in  as{0.user}'.format(client))


@client.event
async def on_message(message):  #these names are from discord documentation
  print('Message here2')
  # print(message)
  # print(message.content[2:])
  if message.author == client.user:
    return  #if message is from the bot itself, ignore

  if message.content.startswith('$hello'):
    await message.channel.send('Hi there! What\'s up?')


client.run(os.environ['TOKEN'])
