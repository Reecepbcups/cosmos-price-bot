#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Coded by CamelJuno 🐪#7465

import discord
import requests
import json
import time
from flask import Flask
from threading import Thread 

app = Flask('')

@app.route('/')
def home():
  return 'Camel is here'

def run():
  app.run(host='0.0.0.0',port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()

client = discord.Client()
def getJUNO2UST():
  headers = {
    'Host': 'api.coingecko.com',
    'Accept': '*/*',
  }
  a = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=juno-network',headers=headers,timeout=10)
  if a.status_code == 200:
    z = json.loads(a.text)[0]['current_price']
    b = json.loads(a.text)[0]['market_cap']
    return z,b
  else:
    getJUNO2UST()

def formatIt(hello):
  suffixes = ["", "", "M", "B", "T"]
  hello = str("{:,}".format(hello))
  commas = 0
  x = 0
  while x < len(hello):
      if hello[x] == ',':
          commas += 1
      x += 1
  return hello.split(',')[0]+'.'+hello.split(',')[1][:-1] + suffixes[commas]

@client.event
async def on_ready():
  print(f'You have logged in as {client}')
  guild = client.get_guild(guildID)
  member = guild.get_member(memberID)
  while(True):
    try:
      JUNO2UST,JunoMC = getJUNO2UST()
      print(JUNO2UST)
      print(JunoMC)
      await member.edit(nick="JUNO $"+str(JUNO2UST))
      time.sleep(1)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="MC: $"+str(formatIt(JunoMC))))
      time.sleep(30)
    except:
      continue

keep_alive()

guildID = 0
memberID = 0
BOT_TOKEN = 'PLACE_AUTH_TOKEN_HERE'
client.run(BOT_TOKEN)