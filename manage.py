from telnetlib import DM
import discord
import datetime
import asyncio

from discord.ext import commands
from discord.utils import get

developer=901518724098568223
Developer=956042267221721119
dt_now= datetime.datetime.now()

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    def is_server(guild_id):
        async def test(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(test)
   
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, message):
        await message.channel.purge()
        await message.send("きれいになったね。")
        await message.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
    
    
    @commands.command()
    @commands.has_permissions(kick_members= True)
    async def kick(self, ctx, user:discord.Member, reason= None):
        if not reason:
            reason= "No reason"
        try:
            embed=discord.Embed(
                title=f"Good BYE",
                description=f"{user.mention} has KICK!!",
                color=0xff0000)
            embed.add_field(name="Reason", value=f"```{reason}```")
            await ctx.send(embed=embed)
            await user.kick(reason=reason)
        except:
            pass
    
    
    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, user:discord.Member, reason= None):
        if not user:
            user= ctx.author
        if not reason:
            reason="No reason"
        try:
            embed=discord.Embed(
                title=f"Good BYE",
                description=f"{user.mention} has BAN!!",
                color=0xff0000
            )
            embed.add_field(name="Reason", value=f"```{reason}```")
            await ctx.send(embed=embed)
            await user.ban(reason=reason)
        except:
            pass
    
    
    @commands.command()
    async def meonly(self, ctx):
        if ctx.author.id==Developer:
            await ctx.send("test")
        else:
            user = await self.bot.fetch_user(956042267221721119)
            embed=discord.Embed(title="serverlist command error", timestamp=ctx.message.created_at)
            embed.add_field(name=f"{ctx.author}, ID: `{ctx.author.id}`", value=f"FROM : DM")
            embed.set_footer(text=str(dt_now))
            await user.send(embed=embed)
            embed = discord.Embed(title="-CommandNotFound", \
            description=f"コマンドが見つかりませんでした。今一度`.help`で確認なさってください。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
    
    
    @commands.command(aliases=["slist"])
    async def serverlist(self, ctx):
        if not ctx.author.id==developer or Developer:
            #user=self.bot.get_user(developer)
            for guild in self.bot.guilds:
                embed=discord.Embed(title="Guild lists",
                                    description=f"**{guild}**\nID : ||`{guild.id}`||\nowner **:** {guild.owner}\nID : ||`{guild.owner.id}`||",
                                    color=0x42caff)
                await ctx.send(embed=embed)
        else:
            user = await self.bot.fetch_user(956042267221721119)
            embed=discord.Embed(title="serverlist command error", timestamp=ctx.message.created_at)
            embed.add_field(name=f"{ctx.author}, ID: `{ctx.author.id}`", value=f"FROM : DM")
            embed.set_footer(text=str(dt_now))
            await user.send(embed=embed)
            
            embed = discord.Embed(title="-CommandNotFound", \
            description=f"コマンドが見つかりませんでした。今一度`.help`で確認なさってください。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def leave(self, ctx, guild_id:int):
        guild = await self.bot.get_guild(guild_id).leave()
        msg = await ctx.send(f"I left")
        await asyncio.sleep(3)
        await msg.delete()
        
    
def setup(bot):
    return bot.add_cog(Manage(bot))
