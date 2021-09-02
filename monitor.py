import os
import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
  var = 1
  channel = client.get_channel(__REPLACE_BY_CHANNEL_ID__)
#  await channel.send('online')
  while True:
    hostname = "__REPLACE_BY_TARGET_IP_OR_HOSTNAME__"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
      print (hostname, 'is up!')
      if var == 0:
        await channel.send('Node is now online.')
      var = 1
    else:
      print (hostname, 'is down!')
      if var == 1:
        await channel.send('Connection to Node was lost.')
      var = 0
    await asyncio.sleep(300)
client.run('__REPLACE_BY_BOT_TOKEN__')
