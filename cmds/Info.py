import discord
import discord.utils
from discord.embeds import Embed
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.embeds import Embed
from discord.ext import commands
import json
import asyncio
from core.classes import Cog_Extension

with open('Setting.json', 'r', encoding='utf8') as jsetting:
    jsetting = json.load(jsetting)
    
footer = jsetting['Footer']

class Info(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    async def check_rank(ctx):
        CEO = ctx.guild.get_role(968887354490237029)
    
    @cog_ext.cog_slash(name="new_training", description=f"Send a new information about training.")
    async def new_training(self, ctx):

        embed=discord.Embed(title=f"Co-Host?", description="Does the training have co-host?", color=0xf1c40f)
        embed.add_field(name="If Yes", value=f"Send the co-host Name out!")
        embed.add_field(name="If Not", value=f"Type `No`/`no`")
        embed.set_footer(text=footer)
        await ctx.reply(embed=embed) 
    
        def check(message):
            return message.author == ctx.author

        msg_cohost = await self.bot.wait_for('message', check=check)

        if not msg_cohost == "No" or not msg_cohost == "no":
            cohost = discord.utils.get(ctx.guild.members, name=msg_cohost)

        elif msg_cohost == "No" or msg_cohost == "No":
            pass

        embed=discord.Embed(title=f"First Trainer", description="Send the first trainer name out.", color=0xf1c40f)
        embed.set_footer(text=footer)
        await ctx.reply(embed=embed) 

        msg_1trainer = await self.bot.wait_for('message', check=check)

        _1trainer = discord.utils.get(ctx.guild.members, name=msg_1trainer)

            
    
def setup(bot):
    bot.add_cog(Info(bot))