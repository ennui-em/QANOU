import discord
import datetime
from discord.ext import commands

developer= ID
Developer= ID
dt_now= datetime.datetime.now()

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command(aliases=["p"])
    @commands.has_permissions(manage_messages= True)
    async def puege(self, ctx, amount:int):
        deleted= await ctx.message.channel.purge(limit= amount+1)
        embed= discord.Embed(title="Message Purged!")
        embed.add_field(name= f"{len(deleted)-1} messages", value= "-Deleted")
        embed.set_footer(text= f"By: {ctx.author}")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(kick_members= True)
    async def kick(self, ctx, user:discord.Member, reason= None):
        if not reason:
            reason= "No reason"
        embed=discord.Embed(
            title=f"Good BYE",
            description=f"{user.mention} has KICK!!",
            color=0xff0000)
        embed.add_field(name="Reason", value=f"```{reason}```")
        await ctx.send(embed=embed)
        await user.kick(reason=reason)
    
    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(self, ctx, user:discord.Member, reason= None):
        if not user:
            user= ctx.author
        if not reason:
            reason="No reason"
        embed=discord.Embed(
            title=f"Good BYE",
            description=f"{user.mention} has BAN!!",
            color=0xff0000
            
        )
        embed.add_field(name="Reason", value=f"```{reason}```")
        await ctx.send(embed=embed)
        await user.ban(reason=reason)
    
    @commands.command()   
    async def leave(self, ctx, guild_id=None):
        if not guild_id:
            guild_id=ctx.guild
        try:             
            guild = self.bot.get_guild(guild_id)         
        except:             
            await ctx.send("Invalid guild")         
        try:
            await ctx.send("I'll leave this server! good bye")
            await guild.leave()             
            print(f"left {guild.name}\n[{guild.id}]")         
        except:             
            await ctx.send("Error leaving")
    
def setup(bot):
    return bot.add_cog(Manage(bot))
