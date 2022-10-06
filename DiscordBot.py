from email import message
from discord.utils import get
import config
import discord
import PythonStock

intents=discord.Intents.default()
intents=discord.Intents().all()
intents.message_content = True
intents.members = True

#bot=discord.Client 是我們與 Discord 連結的橋樑
bot = discord.Client(intents=intents)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    #確認連結TOKEN的BOT是否有誤
    print('目前登入身份：', bot.user)
    #機器人的遊戲狀態，想設什麼都可以
    game = discord.Game('StockBot')
    #機器人的在線狀態
    await bot.change_presence(status=discord.Status.online, activity=game)

#bot=discord.Client 是我們與 Discord 連結的橋樑
bot = discord.Client(intents=intents)

bot.run(config.TOKEN) #TOKEN 在 Discord Developer 的 BOT 頁面


