from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from threading import Timer
from time import sleep
import random


bot1 = Client("bot1", '6379199', '856b127610166f52be190bc9ba5b922b')

@bot1.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("Кaжется, рeйд нaчинается...\nby @dently and @vellogs")
  sleep(1)

bot2 = Client("bot2", '5235407', '07423ead8b4192e7650b14bb532fa037')

@bot2.on_message(filters.command("raid", prefixes="_"))
def spam(self, msg):
 for _ in range(100):
  msg.reply("Кaжется, рeйд нaчинается...\nby @dently and @v3llogs")
  sleep(1)

bot2.run()

