import discord
from discord.ext import commands
import random
import asyncio

# Setup bot with prefix '$' and intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

# Bot visual details
BOT_LOGO = "https://cdn.discordapp.com/attachments/1532300696702025811/1538471654873628692/file_0000000042348211b1d99c7f53f5f1b4.png?ex=6a82cce1&is=6a817b61&hm=20653e7ee60d940fd4b20bb903c2c87e817e47b6b1936af82b6b9d8199047a73&"
SUPPORT_SERVER = "https://discord.gg/qn5Tu34TTd"

# Store warnings locally
warnings_db = {}

@bot.event
async def on_ready():
    stream_activity = discord.Streaming(
        name="Made by NotRyxenYT 👑",
        url="https://www.twitch.tv/discord"
    )
    await bot.change_presence(status=discord.Status.online, activity=stream_activity)
    print(f'Logged in as {bot.user.name}')

@bot.command(name='ai')
async def ai_chat(ctx, *, prompt: str = None):
    if not prompt: return
    prompt_lower = prompt.lower()
    if "hello" in prompt_lower:
        await ctx.reply("Hello there! How can I assist you in Empire Prime?")
    elif "question" in prompt_lower:
        await ctx.reply("🤖 **Empire AI:** Security is the foundation of a thriving community!")

@bot.command(name='nitro')
async def free_nitro(ctx):
    code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
    await ctx.send(f"Unlimited Nitro link generated: https://discord.gift/{code}")

@bot.command(name='warn')
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason: str = "No reason"):
    if member.id not in warnings_db: warnings_db[member.id] = []
    warnings_db[member.id].append(reason)
    await ctx.send(f"⚠️ {member.mention} has been warned: {reason}")

# Replace with your actual token
# bot.run("YOUR_TOKEN")
