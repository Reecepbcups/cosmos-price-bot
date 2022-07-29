#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import discord
import requests
import json
import time

client = discord.Client()
def getJUNOOsmosis():
  headers = {
    'Host': 'api-osmosis.imperator.co',
    'Accept': '*/*'
  }
  a = requests.get('https://api-osmosis.imperator.co/tokens/v2/JUNO',headers=headers,timeout=20)
  if a.status_code == 200:
    z = round(json.loads(a.text)[0]['price'],2)
    y = round(json.loads(a.text)[0]['price_24h_change'],2)
    if z == None:
      getJUNOOsmosis()
    else:
      return z,y
  else:
    getJUNOOsmosis()

@client.event
async def on_ready():
  print(f'You have logged in as {client}')
  guild = client.get_guild(guildID)
  member = guild.get_member(memberID)
  while(True):
    try:
      price,PriceChange = getJUNOOsmosis()
      await member.edit(nick="JUNO $"+str(price))
      time.sleep(1)
      if PriceChange > 0:
        PriceChange = '+'+str(PriceChange)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Δ 24h: "+str(PriceChange)+"%"))
      time.sleep(28)
    except:
      continue

guildID = 0
memberID = 0
BOT_TOKEN = 'PLACE_AUTH_TOKEN_HERE'
client.run(BOT_TOKEN)