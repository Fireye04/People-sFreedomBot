import discord
import random
import pickle
import asyncio

from discord.ext import commands
client = commands.Bot(command_prefix=".")
client.remove_command('help')
emojis = ["👍","👎"]
target_server_id = 768178215251476510




@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='with politics'))
    print("Ready")


@client.command(aliases=["DM", "dm"])
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


@client.command(aliases=["i"])
async def init(ctx):

    server = client.get_guild(target_server_id)
    channel = server.get_channel(768233149414768641)
    if not isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("Private command only please use in DMs. If you don't have a DM with me, use the .DM"
                       " command (.dm @mention hello)")
    else:
        print(str(ctx.message.author))
        await ctx.send("Are you a BTN Student? (please respond 'yes' or 'no'.)")
        try:
            btnStudent = await client.wait_for('message', timeout=30)
            if btnStudent.content == "yes" or btnStudent.content == "Yes":
                member = server.get_member(ctx.message.author.id)
                var = discord.utils.get(server.roles, name = "BTN")
                await member.add_roles(var)
                x = "Is a BTN student"
            else:
                x = "Not BTN (" + str(btnStudent.content) + ")"

            await asyncio.sleep(1)

            await ctx.send("Do you support BASIS's current student council? (please respond 'yes' or 'no')")

            try:
                stucoSupport = await client.wait_for('message', timeout=30)
                if stucoSupport.content == "yes" or stucoSupport.content == "Yes":
                    member = server.get_member(ctx.message.author.id)
                    var = discord.utils.get(server.roles, name = "Stuco")
                    await member.add_roles(var)
                    y = "supports stuco. excersise caution"
                else:
                    member = server.get_member(ctx.message.author.id)
                    var = discord.utils.get(server.roles, name = "Interested Member")
                    await member.add_roles(var)
                    y = "Does not support stuco"

                await asyncio.sleep(1)

                await ctx.send("What IRL Political party do you identify with? (democrat, republican, libertarian, etc...)")
                try:
                    politicalView = await client.wait_for('message', timeout=30)

                    await asyncio.sleep(1)

                    await channel.send(str(ctx.message.author))
                    await channel.send("~~~")
                    await channel.send(x)
                    await channel.send(y)
                    await channel.send(str(politicalView.content))
                    await channel.send(" ")
                except TimeoutError:
                    await ctx.send("Timed out. Please do the command .init to restart the process")
            except TimeoutError:
                await ctx.send("Timed out. Please do the command .init to restart the process")
        except TimeoutError:
            await ctx.send("Timed out. Please do the command .init to restart the process")


@client.event
async def on_member_join(member):
    await member.send("Welcome to The People's freedom party! We are the first and only political party at BTN."
                      " Our goal is to put candidates who will enact the view of the people into the student council.")
    server = client.get_guild(target_server_id)
    channel = server.get_channel(768233149414768641)
    print(str(member))
    await member.send("Are you a BTN Student? (please respond 'yes' or 'no'.)")
    try:
        btnStudent = await client.wait_for('message', timeout=30)
        if btnStudent.content == "yes" or btnStudent.content == "Yes":
            member = server.get_member(member.id)
            var = discord.utils.get(server.roles, name = "BTN")
            await member.add_roles(var)
            x = "Is a BTN student"
        else:
            x = "Not BTN (" + str(btnStudent.content) + ")"

        await asyncio.sleep(1)

        await member.send("Do you support BASIS's current student council? (please respond 'yes' or 'no')")

        try:
            stucoSupport = await client.wait_for('message', timeout=30)
            if stucoSupport.content == "yes" or stucoSupport.content == "Yes":
                member = server.get_member(member.id)
                var = discord.utils.get(server.roles, name = "Stuco")
                await member.add_roles(var)
                y = "supports stuco. excersise caution"
            else:
                member = server.get_member(member.id)
                var = discord.utils.get(server.roles, name = "Interested Member")
                await member.add_roles(var)
                y = "Does not support stuco"

            await asyncio.sleep(1)

            await member.send("What IRL Political party do you identify with? (democrat, republican, libertarian, etc...)")
            try:
                politicalView = await client.wait_for('message', timeout=30)

                await asyncio.sleep(1)

                await channel.send(str(member))
                await channel.send("~~~")
                await channel.send(x)
                await channel.send(y)
                await channel.send(str(politicalView.content))
                await channel.send(" ")
            except TimeoutError:
                await member.send("Timed out. Please do the command .init to restart the process")
        except TimeoutError:
            await member.send("Timed out. Please do the command .init to restart the process")
    except TimeoutError:
        await member.send("Timed out. Please do the command .init to restart the process")





client.run("")