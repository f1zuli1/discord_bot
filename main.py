import discord
from bot_logic import gen_pass 
gen_pass(10)

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Merhaba")
    elif message.content.startswith('bye'):
        await message.channel.send("bye")
    elif message.content.startswith('selam'):
        await message.channel.send("selam!")
    elif message.content.startswith('Selam'):
        await message.channel.send("Selam!")
    elif message.content.startswith('merhaba'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('Merhaba'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('nasilsin'):
        await message.channel.send("Iyiyim")
    elif message.content.startswith('Nasilsin'):
        await message.channel.send("Iyiyim")
    else:
        await message.channel.send(message.content)

client.run("Token")
