import discord
import random
import asyncio
import datetime
import dateutil.parser
from discord.ext import commands

developer= ID
Developer= ID
dt_now= datetime.datetime.now()

class Maincmd(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self._last_member= None
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(
        title="HELP FOR ENGLISH",
        description=(
            f"Example\n\
            `command[aliase]` **:** Operation content\n\
            \n\
            :partying_face: **VARIETY**\n\
            `fortune[kuji]` **:** Fortune telling\n\
            `now`, `なう` **:** Reacts without a prefix\n\
            \n\
            :tools: **TOOL**\n\
            `help` **:** this command\n\
            `helpja` **:** Help for Japanese\n\
            `about` **:** About this bot\n\
            `ping` **:** Check bot's ping\n\
            `avatar` **:** Get the user avatar\n\
            `banner[b]` **:** Get the banner if you have\n\
            `gifbanner[gb]` **:** Get the GIFbanner if you have\n\
            `track` **:** Get URL of the Spotify song your listening to\n\
            `spotify[sp]` **:** Information on the Spotify song you are listening to\n\
            `userinfo` **:** Get info about user\n\
            `serverinfo[si]` **:** Get info about server\n\
            \n\
            :gear: **MANAGE**\n\
            `purge[p]` **:** Delete message by Number\n\
            `kick id *(reason)` **:** Member kick from your server\n\
            `ban id *(reason)` **:** Member ban from your server\n\
            "),
        color=0x6dc1d1
        )
        embed.add_field(
        name="*(reason)", 
        value=f"-Reason to use command(Possible without)",
        inline=False)
        embed.set_footer(text=str(f"By: {ctx.author}"))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def helpja(self, ctx):
        embed= discord.Embed(
            title= "ヘルプ　日本向け",
            description= 
                f"見方\n\
                `コマンド[エイリアス]` **:** 実行内容\n\
                \n\
                :partying_face: **バラエティ**\n\
                `なう`, `now` **:** プレフィックス無しで反応して、現現在時刻を表示。\n\
                `fortune[kuji]` **:** おみくじ\n\
                \n\
                :tools: 便利\n\
                `help` **:** 英語のヘルプコマンド\n\
                `helpja` **:** このコマンド\n\
                `about` **:** このボットについて\n\
                `ping` **:** ボットとのレイテンシを測定\n\
                `avatar` **:** ユーザーのアバターを表示\n\
                `banner[b]` **:** ユーザーのバナーを表示。もしあれば\n\
                `gifbanner[gb]` **:** ユーザーのGIFバナーを表示。もしあれば\n\
                `track` **:** ユーザーのSpotify楽曲のURLを表示\n\
                `spotify[sp]` **:** Spotify楽曲の詳細を表示\n\
                `userinfo[ui]` **:** ユーザーの詳細を表示\n\
                `serverinfo[si]` **:** サーバーの詳細を表示\n\
                \n\
                :gear: **管理**\n\
                `purge[p]` **:** 指定した分メッセージを削除\n\
                `kick id *(reason)` **:** サーバーからメンバーをキック(kick)\n\
                `ban id *(reason)` **:** サーバーからメンバーをバン(ban)\n\
                \n\
                ",
            color= 0x6dc1d1)
        embed.add_field(name= "*(reason)",
                        value= "コマンドを使う理由(無くても可)")
        embed.set_footer(text=str(f"By: {ctx.author}"))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def about(self, ctx):
        user= self.bot.get_user(developer)
        members= 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        embed= discord.Embed(
            title= "-> src in github",
            color= 0x6dc1d1,
            url= "https://github.com/ennui-em/QANOU/tree/main"
            )
        embed.add_field(name= "Customers",
                        value= f"Servers **:** `{str(len(self.bot.guilds))}`\n\
                                Members **:** `{str(members)}`", inline= False)
        embed.add_field(name= "Dev", value= f"{user.mention}", inline= False)
        embed.set_author(name= "About this bot")
        embed.set_footer(text=f"By: {str(ctx.author)}")
        await ctx.send(embed=embed)
        await ctx.send("discord.gg/daze")
    
    @commands.command()
    async def fortune(self, ctx):
        result = [":clap: 大吉", ":wink: 吉", ":sweat_smile: 中吉", ":smirk: 小吉", ":sweat: 凶", ":joy::thumbsup: 大凶"]
        embed= discord.Embed(title=f"{random.choice(result)}", color= 0x6dc1d1)
        embed.set_footer(text= f"By: {str(ctx.author)}")
        await ctx.reply(embed=embed, mention_author= False)
    
    @commands.command()
    async def ping(self, ctx):
        pingpong= f"Latency-{round(self.bot.latency * 1000)}m/s"
        embed= discord.Embed(title= f":ping_pong: Pong!",description= f"{pingpong}",  color= 0x6dc1d1)
        embed.set_footer(text= f"By: {str(ctx.author)}")
        await ctx.reply(embed= embed, menton_author= False)
    
    @commands.command(aliases=["icon"])
    async def avatar(self, ctx, user:discord.Member=None):
        if not user:
            user= ctx.author
        avatar= user.avatar_url
        embed= discord.Embed(title= "Avatar Link", description= f"{user.mention}'s Avatar",  color= 0x6dc1d1, url= avatar)
        embed.set_author(name= str(user), icon_url= avatar)
        embed.set_image(url= avatar)
        embed.set_footer(text= f"{str(ctx.auhtor)}")
        await ctx.send(embed= embed)
    
    @commands.command(aliases=["b"])
    async def banner(self, ctx, user:discord.Member=None):
        if not user:
            user= ctx.author
        try:
            req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
            banner_id = req["banner"]
            if banner_id:
                banner_url= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            embed= discord.Embed(title= "Banner Link", description= f"{user.mention}'s banner", color= 0x6dc1d1, url= banner_url)
            embed.set_image(url= banner_url)
            embed.set_footer(text= str(f"By : {ctx.author}"))
            await ctx.send(embed= embed)
        except:
            embed= discord.Embed(title= "Have you set banner?")
            embed.set_footer(text=str(f"By: {ctx.author}"))
            await ctx.send(embed= embed)
    
    @commands.command(aliases=["gb"])
    async def gifbanner(self, ctx, user:discord.Member=None):
        if not user:
            user= ctx.author
        try:
            req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
            banner_id = req["banner"]
            if banner_id:
                banner_url= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif?size=1024"
            embed= discord.Embed(title= "Banner Link", description= f"{user.mention}'s banner", color= 0x6dc1d1, url= banner_url)
            embed.set_image(url= banner_url)
            embed.set_footer(text= str(f"By : {ctx.author}"))
            await ctx.send(embed= embed)
        except:
            embed= discord.Embed(title= "Have you set banner?")
            embed.set_footer(text=str(f"By: {ctx.author}"))
            await ctx.send(embed= embed)
    
    @commands.command()
    async def track(self, ctx, user:discord.Member=None):
        if not user:
            user=ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        
        if spotify_result is None:
            await ctx.send(f"{user.name} is not listening to SPotify!")
        
        if spotify_result:
            await ctx.send(f"https://open.spotify.com/track/{spotify_result.track_id}")
    
    @commands.command(aliases=["sp"])
    async def spotify(self, ctx, user:discord.Member=None):
        if not user:
            user=ctx.author
        spotify_result= next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        
        if spotify_result is None:
            await ctx.send(f"{user.name} is not listening to Spotify!")
        
        if spotify_result:
            embed=discord.Embed(
                title=f"{spotify_result.title}",
                color=0x6dc1d1,
                url=f"https://open.spotify.com/track/{spotify_result.track_id}"
                )
            embed.set_thumbnail(url=spotify_result.album_cover_url)
            embed.add_field(name="Name", value=f"```{spotify_result.title}```")
            artists = spotify_result.artists
            if not artists[0]:
                re_result=spotify_result.artist
            else:
                re_result = ',\n'.join(artists)
            embed.add_field(name="Artist[s]", value=f"```{re_result}```")
            embed.add_field(name="Album", value=f"```{spotify_result.album}```", inline=False)
            embed.add_field(name="Time", value=f"```{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}```")
            embed.add_field(name="URL", value=f"```https://open.spotify.com/track/{spotify_result.track_id}```", inline=False)
            embed.set_footer(text=f"By: {str(ctx.author)}")
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, user:discord.Member= None):
        if not user:
            user= ctx.author
        date_format="%Y/%m/%d %H:%M:%S"
        avatar= user.avatar_url
        embed= discord.Embed(title= f"{user} information", description= f"**ID : `{user.id}`**", color= 0x6dc1d1)
        embed.set_thumbnail(url= avatar)
        embed.add_field(name= "Name", value= f"`{user}`",inline= True)
        embed.add_field(name= "Nickname", value= f"`{user.display_name}`", inline= True)
        embed.add_field(name= "Bot?", value= f"`{user.bot}`", inline= True)
        if len(user.roles) > 1:
            role_string= " ".join([r.mention for r in user.roles][1:])
        embed.add_field(name= f"Role[s] -`{len(user.roles)-1}`", value= role_string, inline=False)
        embed.add_field(name= "Createion Account", value= f"`{user.created_at.strftime(date_format)}`", inline= True)
        embed.add_field(name= "Joined Server", value= f"`{user.joined_at.strftime(date_format)}`", inline= True)
        try:
            req= await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid= user.id))
            banner_id= req["banner"]
            if banner_id:
                banner_url= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
                embed.set_image(url= banner_url)
                embed.set_footer(text= f"By: {str(ctx.author)}  [Banner is png file!]")
        except:
            embed.set_footer(text= f"By: {str(ctx.author)}")
        await ctx.send(embed= embed)
    
    @commands.command(aliases=["si"])
    async def serverinfo(self, ctx):
        guild= ctx.guild
        date_f= "%Y/%m/%d"
        region= str(guild.region)
        mcount= str(guild.member_count)
        ucount= str(sum(1 for member in guild.members if not member.bot))
        bcount= str(sum(1 for member in guild.members if member.bot))
        tchannels= len(guild.text_channels)
        vchannels= len(guild.voice_channels)
        categories= len(guild.categories)
        roles= [role for role in guild.roles]
        emojis= [emoji for emoji in guild.emojis]
        embed= discord.Embed(title=f"{guild.name} information", description= f"**Server id : `{guild.id}`**", color= 0x6dc1d1)
        embed.set_thumbnail(url= guild.icon_url)
        embed.add_field(name= "Owner", value= f"> {guild.owner.mention}")
        embed.add_field(name= "Region", value= f"> `{region}`")
        embed.add_field(name= "Emojis", value= f"> Emojis: `{len(emojis)}`")
        
        embed.add_field(name= "Boost", 
                        value= f"> boost **:** `{guild.premium_subscription_count}`\n> Tier **:** `{guild.premium_tier}`")
        
        embed.add_field(name= "Roles", value= f"> Role **:** `{len(roles)}`", inline= True)
        embed.add_field(name= "Createion", value= f"> `{guild.created_at.strftime(date_f)}`", inline=True)
        
        embed.add_field(name= "Members", value= f"> Member **:** `{mcount}`\n> User: `{ucount}`\n> Bot: `{bcount}`")
        embed.add_field(name= "Channels", 
                        value= f"> Channel **:** `{tchannels+vchannels}`\n> Text **:** `{tchannels}`\n> Voice **:** `{vchannels}`\n> Category **:** `{categories}`",inline= True)
        try:
            req= await self.bot.http.request(discord.http.Route("GET", "/guilds/{sid}", sid= guild.id))
            banner_id= req["banner"]
            if banner_id:
                banner_url= f"https://cdn.discordapp.com/banners/{guild.id}/{banner_id}.png?size=1024"
                embed.set_image(url= banner_url)
                embed.set_footer(text= f"By: {str(ctx.author)}  [Banner is png file!]")
        except:
            embed.set_footer(text= f"By: {str(ctx.author)}")
        await ctx.send(embed= embed)
    

def setup(bot):
    return bot.add_cog(Maincmd(bot))
