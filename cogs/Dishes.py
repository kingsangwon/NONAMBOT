import discord
from discord.ext import commands

from module.dish import dishFromDate

class Dish(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name='급식')
    async def dish(self, ctx, ymd):
        breakfast=dishFromDate(ymd, 1)
        lunch=dishFromDate(ymd, 2)
        dinner=dishFromDate(ymd, 3)
        embed=discord.Embed(title="급식", description=f'{ymd} 군산제일고등학교 급식입니다.', color=0x29428b)
        embed.add_field(
            name='조식',
            value='\n'.join(breakfast)
        )
        embed.add_field(
            name='중식',
            value='\n'.join(lunch)
        )
        embed.add_field(
            name='석식',
            value='\n'.join(dinner)
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Dish(bot))
