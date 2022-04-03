import discord
import datetime
from discord.ext import commands

developer= ID
Developer= ID
dt_now= datetime.datetime.now()

class Main2(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        user= self.bot.get_user(developer)
        User= self.bot.get_user(Developer)
        pingpong = f"latency : `{round(self.bot.latency * 1000)}`m/s"
        embed=discord.Embed(title="Successfully Connected",description=f"Developer : {user.mention}, {User.mention}\n{pingpong}", color=0x6dc1d1)
        embed.set_footer(text=f" {dt_now.month}月 {dt_now.day}日 {dt_now.hour} : {dt_now.minute} - {dt_now.minute}秒")
        await user.send(embed=embed)
    
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content=="なう" or "now":
          """未開発（めんどくさい）"""
            await message.reply(   mention_author= False)
            
    #Errorhandling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            embed = discord.Embed(title="-MissingPermissions", \
                description=f"権限不足ですよ。出直せバカ", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
            embed = discord.Embed(title="-BotMissingPermissions", \
            description=f"当botの権限が不当に制限されています。信用ないならなぜ入れたんです？", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
            embed = discord.Embed(title="-CommandNotFound", \
            description=f"コマンドが見つかりませんでした。今一度`.help`で確認なさってください。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
            embed = discord.Embed(title="-MemberNotFound", \
                description=f"指定されたユーザーが発見されませんでした。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.BadArgument):
            embed = discord.Embed(title="-BadArgument", \
            description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed) 
        elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="-BadArgument", \
            description=f"必要な引数が足りません。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.CheckFailure):
            embed = discord.Embed(title="-CheckFailure", \
            description=f": defined", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        else:
            raise error
    
def setup(bot):
    return bot.add_cog(Main2(bot))
