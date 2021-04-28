import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('TEXT HERE')
      print(f"> Mensagem enviada para | Message sent to : {user.name} <")
    except:
       print(f"> MSG SENT TO  | MSG DECLINED FOR : {user.name} <")
       
client.run('TOKENHERE', bot=False)
