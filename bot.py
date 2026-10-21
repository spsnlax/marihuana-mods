import discord
import json

intents = discord.Intents.default()
intents.members = True  # Obligatorio para leer el total de miembros

client = discord.Client(intents=intents)

# Token de Marihuano Bot
TOKEN = "MTU2MjM1NjUyNjg5Nzk1ODk4Mg.GgrA2x.T4Ihik7U44TcvBKZZOr4UfY7Tx2hk3hmM1ibfU"

def actualizar_stats(guild):
    stats = {
        "total_members": guild.member_count
    }
    with open("stats.json", "w") as f:
        json.dump(stats, f)
    print(f"[✔] Miembros totales actualizados en stats.json: {guild.member_count}")

@client.event
async def on_ready():
    print(f'🤖 Bot encendido y conectado como: {client.user}')
    for guild in client.guilds:
        actualizar_stats(guild)

@client.event
async def on_member_join(member):
    actualizar_stats(member.guild)

@client.event
async def on_member_remove(member):
    actualizar_stats(member.guild)

client.run(TOKEN)