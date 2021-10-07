import discord
from discord.ext import commands
import ship
import auth
import space



myShip = ship
myShip.initSave()


bot = commands.Bot(command_prefix=".")
@bot.command()

async def hello(ctx):
    await ctx.reply('Hello')
    myShip.save()

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)
    myShip.save()

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')
    myShip.save()

@bot.command()
async def power(ctx):
    await ctx.reply("Power: " + str(myShip.power))
    myShip.save()

@bot.command()
async def fuel(ctx):
    await ctx.reply("Fuel: " + str(myShip.fuel))
    myShip.save()

@bot.command()
async def shield(ctx):
    await ctx.reply("Shield: " + str(myShip.shield))
    myShip.save()

@bot.command()
async def money(ctx):
    await ctx.reply("Money: " + str(myShip.money))
    myShip.save()

@bot.command()
async def buyfuel(ctx):
    buy = True
    buy = myShip.buyFuel(buy)
    if buy:
        await ctx.reply("Fuel purchased")
        await ctx.reply("Fuel: " + str(myShip.fuel))
        
    else:
        await ctx.reply("Need more money")
    myShip.save()

@bot.command()
async def save(ctx):
    myShip.save()
    await ctx.reply("Saved")

@bot.command()
async def stats(ctx):
    await ctx.reply("Power: " + str(myShip.power))
    await ctx.reply("Fuel: " + str(myShip.fuel))
    await ctx.reply("Shield: " + str(myShip.shield))
    await ctx.reply("Money: " + str(myShip.money))
    myShip.save()

# Private message the bot
@bot.command()
async def dm(ctx):
    user = ctx.author
    await user.send("Welcome to the private chat!")
    myShip.save()

@bot.command()
async def location(ctx):
    await ctx.reply("Your ship is located at " + str(myShip.locx) + "," + str(myShip.locy))
    myShip.save()


@bot.command()
async def map(ctx):
    space.makeMap()
    await ctx.reply("Map ready")
    myShip.save()


async def commands(ctx):
    await ctx.reply('commands, power, fuel, shield, money, stats, buyfuel, location, map, hello, ping, add, save, dm')
    myShip.save()



bot.run(auth.botAuth)