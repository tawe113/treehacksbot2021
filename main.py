import discord
import random as rd
import pandas as pd
import datetime
from datetime import datetime, timezone
import pytz
import asyncio

carbon = pd.read_csv('carbontonnes.csv')
#carb.set_index('Company')

#time in pst
tz_SF = pytz.timezone('PST8PDT') 

client = discord.Client()

async def background_guide():
  await client.wait_until_ready()
  gen_channel = client.get_channel(id='810013571891068932')
  while not client.is_closed:
    await client.send_message(gen_channel, "hello!")
    await asyncio.sleep(5)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!funfact'):
      funfacts = []
      with open('treehax1.txt') as f:
        for line in f:
          funfacts.append(line)

      index = rd.randint(0, len(funfacts) - 1)
      fact = funfacts[index]
      await message.channel.send(fact)

    if message.content.startswith('!action'):
      actions = []
      with open('action.txt') as f:
        for line in f:
          actions.append(line)

      index1 = rd.randint(0, len(actions) - 1)
      action = actions[index1]
      await message.channel.send(action) 
      
    utc_dt = datetime.now(timezone.utc) # UTC time
    dt = utc_dt.astimezone() # local time
    dt.now().hour  
    
    if message.content.startswith('!worldwide'):
      worldwide = round(((dt.now(tz_SF).hour)*1331*60*60 + dt.now(tz_SF).minute*1331*60 + dt.now(tz_SF).second*1331)*2204/1000000)
      
      await message.channel.send(str(worldwide) + 
      ' million pounds of CO2 have been emitted worldwide today. That is equivalent to ' + str(round(worldwide * 1000000/220000)) + ' blue whales.')

    if message.content.startswith('!time'):
      await message.channel.send(datetime.now(tz_SF))
    
    def ton():
      c = ''
      for i in range(4):
        c += (str(round(1000000000*(dt.now(tz_SF).hour*carbon['per hour'][i] + dt.now(tz_SF).minute*carbon['per minute'][i] + dt.now(tz_SF).second*carbon['per second'][i])*2204, 2)) + ' pounds of CO2 emitted by ' + str(carbon['Company'][i]) + " today.\n") 
      return c

    if message.content.startswith('!carbon'):
      await message.channel.send(str(ton()))

    def whale():
      c = ''
      for i in range(4):
        c += (str(round(1000000000*(dt.now(tz_SF).hour*carbon['per hour'][i] + dt.now(tz_SF).minute*carbon['per minute'][i] + dt.now(tz_SF).second*carbon['per second'][i])*2204/220000, 2)) + ' blue whales of CO2 emitted by ' + str(carbon['Company'][i]) + " today\n") 
      return c

    if message.content.startswith('!whale'):
      await message.channel.send(str(whale()))
    
    if message.content.startswith('!jarf'):
      await message.channel.send("i just jarfed in my mouth")

    if message.content.startswith('!uwu'):
      await message.channel.send("ur so cute ahah hah <3. but you know what's not cute? carbon emissions.")
    
    if message.content.startswith('!janice'):
      await message.channel.send("Janice cam!")


    if message.content.startswith('!help'):
      await message.channel.send('Here are a list of commands you can have the bot run:\n-- !funfact gives a random fun fact about climate change. \n-- !action gives an action item you can take to combat climate change. \n-- !worldwide shows the amount of pounds (in millions) of CO2 emissions produced today worldwide, and its weight equivalent in blue whales. One blue whale weighs 220,000 pounds. \n-- !carbon shows how many pounds of CO2 have been produced today by the four biggest oil companies in the world. \n-- !whale shows the equivalent of CO2 emissions by the four biggest oil companies in blue whales. \n-- There are a number of hidden commands as well! Have fun playing around with them :)')

    bot_mention = ["bot", "carbonbot"]
    if any(word in message.content for word in bot_mention):
      await message.channel.send("Did someone say my name?")   
      

    

    

    




TOKEN = "ODEwMDEyMTg1NDU1NjI0MTky.YCdcog.OH6jJSc6x4BC2N34HVcUdhZMjVs"
client.loop.create_task(background_guide())
client.run(TOKEN)


