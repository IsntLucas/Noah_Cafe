import discord
from discord.ext import commands
from discord_slash import SlashCommand
import json
import os
import asyncio

intents = discord.Intents().all()

bot = commands.Bot(command_prefix="Noah/", intents=intents)
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)

with open('Setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

footer = jdata['Footer']

@bot.event
async def on_ready():
    servers = len(bot.guilds)
    print(" >>> Noah-Cafe Bot is Online Now.<<<")
    
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Starting Up'))
    await asyncio.sleep(60)
    
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Setting Up'))
    await asyncio.sleep(12)
    
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Connecting to OWCA'))
    await asyncio.sleep(33)

    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Loading Data'))
    await asyncio.sleep(33)
    
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Done | Prepared for Service'))
    await asyncio.sleep(12)
    
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('/help | See about me'))

#command or bot error message
@bot.event
async def on_command_error(ctx, error):
    with open('Setting.json', 'r', encoding='utf8') as jsetting:
        jsetting = json.load(jsetting)
        
    footer = jsetting['Footer']

    if isinstance(error, commands.CommandNotFound):

        embed=discord.Embed(title=f"Do Slash Command", description=f"We are now trasnfered all command to slash command. Do `/help` to see commands list.", color=0xe74c3c)
        embed.set_footer(text=footer)
        await ctx.reply(embed=embed)

    
@slash.slash(name="latency", description=f"Show bot's latency.")
async def latency(ctx):
    with open('Setting.json', 'r', encoding='utf8') as jsetting:
        jsetting = json.load(jsetting)
        
    footer = jsetting['Footer']

    snow_yprm = bot.get_user(880076631446814812)
    embed=discord.Embed(title=f"Latency", description=f"Now latency is **{round(bot.latency*1000)} ms.**", color=0xf1c40f)
    embed.set_footer(text=footer)
    await ctx.reply(embed=embed)
    
#reload comamnds (one for all)
@slash.slash(name="reload", description="Re-load all commands.")
async def reload(ctx):

    bot.reload_extension(f'cmds.Info')
    bot.reload_extension(f'cmds.Help')
    bot.reload_extension(f'cmds.Ticket')
    embed = discord.Embed(title=f"All Commands Re-loadded",color=0xf1c40f)
    embed.set_footer(text=footer)
    await ctx.reply(embed=embed)


    


#run cogs
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

#token
if __name__ == "__main__":
    bot.run(jdata['Token'])