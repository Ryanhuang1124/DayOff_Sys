import discord
from discord.ext import commands
import datetime
import json
with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


bot = commands.Bot(command_prefix= '!')
client=discord.Client()

today = datetime.date.today()

@bot.command()
async def 出團時間(ctx):
    with open('dayoffstate.json',mode='r',encoding='utf8')as weekstate:
        raidstate=json.load(weekstate)

    channel=bot.get_channel(765238860342493235)

    if today.weekday()<3:
        isweek='本週'
        n=today.weekday()
        timeDelta = datetime.timedelta(days=n)
        monday=today-timeDelta
        oneday=datetime.timedelta(days=1)
        tuesday=monday+oneday
        wesday=tuesday+oneday
    else :
        isweek='下週'
        n=today.weekday()
        timeDelta = datetime.timedelta(days=7-n)
        monday=today-timeDelta
        oneday=datetime.timedelta(days=1)
        tuesday=monday+oneday
        wesday=tuesday+oneday

    await channel.send(
        f'{isweek}   \n'
        f"星期一  ({monday.year}/{monday.month}/{monday.day})  :  {raidstate['1']}\n"
        f"星期二  ({tuesday.year}/{tuesday.month}/{tuesday.day})  :  {raidstate['2']}\n"
        f"星期三  ({wesday.year}/{wesday.month}/{wesday.day})  :  {raidstate['3']}\n"
    )

@bot.command()
async def 休團(ctx,*,weekday):
   if ctx.author.name == 'Ryanhuang' :
        with open('dayoffstate.json',mode='r',encoding='utf8') as weekstate:
            raidstate=json.load(weekstate)

        if weekday == "1":
           raidstate['1']='休團'
           await ctx.send('Done')

        elif weekday == "2" :
           raidstate['2']='休團'
           await ctx.send('Done')

        elif weekday == "3" :
           raidstate['3']='休團'
           await ctx.send('Done')
        elif weekday == "All" :
            raidstate['1']='休團'
            raidstate['2']='休團'
            raidstate['3']='休團'
            await ctx.send('Done')
        elif weekday == "Cancel":
            raidstate['1']='正常開團'
            raidstate['2']='正常開團'
            raidstate['3']='正常開團'
            await ctx.send('Done')
        
        ret=json.dumps(raidstate)
        with open('dayoffstate.json','w') as update:
            update.write(ret)


@bot.command()
async def 請假(ctx,*,weekday):
    with open('thisweek.json','r') as output:
            olddayoff =json.load(output)
    if  (weekday!= '1') & (weekday!= '2') & (weekday!= '3') :
        await ctx.send('輸入錯誤,只能是 1、2、3 ')
    elif weekday=='1' :
        olddayoff[ctx.author.name]='星期一'
    elif weekday=='2' :
        olddayoff[ctx.author.name]='星期二'
    elif weekday=='3' :
        olddayoff[ctx.author.name]='星期三'
        


    




@bot.event
async def on_ready():
    print(">>bot online")




bot.run(jdata['Token'])