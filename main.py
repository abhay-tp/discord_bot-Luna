import discord
from discord.ext import commands
import requests
import json
import os
from keep_alive import keep_alive

import operation as op

client=commands.Bot(command_prefix="luna.")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.command()#Astronomy
async def space(ctx):
  response=requests.get("https://api.nasa.gov/planetary/apod?api_key=NMuJ7d7OovKcKU3IX5qLRxqe3LatVWor9nqvGdeA") 
  response=json.loads(response.text)
  date_=response["date"]
  explaination=response["explanation"]
  url=response["url"]
  embed=discord.Embed(title=f"**Astronomy of the day {date_}**",description=f"{explaination}\n\n``For Animation/image`` [**Click here**]({url})",colour=discord.Color.from_rgb(240, 248, 255))
  embed.set_image(url=url)
  embed.set_footer(text="provided by NASA Open Innovation Team")
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/5396/5396631.png")
  await ctx.send(embed=embed)


@client.command()#oxford dictionary
async def find(ctx,*, text):
  if text == "help!":
    embed=discord.Embed(title="``Syndax``",description="**``/find <word>``**\nExample  ::  ``/find love`` \n*sentences are not allowed pls bare with me..*",colour=discord.Color.from_rgb(240, 248, 255))
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3820/3820259.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    return
  response = requests.get('https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/{}'.format(text.lower()), headers = {'app_id' :"d1434e5c" , 'app_key' : '80eb0c0742db8f8b41afc27daa61bb04'})
  Data=json.loads(response.text)

  if Data!={'error': 'No entry found matching supplied source_lang, word and provided filters'}:
    word=Data['id']
    provider=Data['metadata']["provider"]
    try:
      origin=Data["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]
    except:
      origin="not available"
    meaning=Data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    try:
      example=Data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"]
    except:
      example="Sorry,No examples available"
    embed = discord.Embed(
      Title="",
      description = ""
      ,colour = discord.Colour.from_rgb(210, 0, 0))
    
    embed.set_author(name="Explaining {}".format(word),icon_url="https://cdn-icons-png.flaticon.com/128/5361/5361003.png")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/5363/5363132.png")
    embed.set_image(url='https://cdn-icons-png.flaticon.com/128/5363/5363099.png')
    embed.add_field(name='Defintion',value='{}'.format(meaning),inline=False)
    embed.add_field(name='Origin of word',value='{}'.format(origin),inline=False)
    embed.add_field(name='Example.',value='{}'.format(example),inline=False)
    embed.add_field(name='Provider',value="{}".format(provider),inline=False)
    await ctx.send(embed = embed)
  else:
    error=Data["error"]
    embed = discord.Embed(
      Title="",
      description = ""
      ,colour = discord.Colour.red()
    )
    embed.set_author(name="ERROR!!")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/5361/5361035.png")
    embed.set_image(url='https://cdn-icons-png.flaticon.com/128/5361/5361019.png')
    embed.add_field(name="{}".format(error),value="sorry,try again\n*Type ``/find help!`` for tutorial*",inline=False) 
    await ctx.send(embed=embed)



@client.command()#Covid Guide
async def covid_ins(ctx):
  await ctx.send(embed=op.make_emb(title="**Guide line to avoid Covid-19**",des="***prepared by [Centers For Disease Control and Prevention](https://www.cdc.gov/)***",thumbnail="https://t3.ftcdn.net/jpg/03/49/80/86/240_F_349808617_xjCQqPU6wf4M26ETFuTCsMIMordVYRLM.jpg",color="68, 52,235"))
  
  await ctx.send(embed=op.make_emb(title="**Protect Unvaccinated Family Members**",des="Some people in your family need to continue to take steps to protect themselves from COVID-19, including\n~\t***Anyone not fully vaccinated, including children under 12*** who   cannot be vaccinated yet\n~\tPeople with weakened immune systems or underlying medical   conditions",thumbnail="https://cdn-icons-png.flaticon.com/128/3576/3576937.png",color="68, 52,235"))

  await ctx.send(embed=op.make_emb(title="**Get Vaccinated**",des="[Authorized COVID-19 vaccines](https://selfregistration.cowin.gov.in/) can help protect you from ***COVID-19***.\n~ You should get a ***COVID-19 vaccine*** as soon as you can.\n~ Once you are fully vaccinated, you may be able to start doing some things that you had stopped doing because of the pandemic.",thumbnail="https://cdn-icons-png.flaticon.com/128/5419/5419329.png",color="68, 52,235"))
  
  await ctx.send(embed=op.make_emb(title="**Wear a mask**",des="If you are not ***fully vaccinated and aged 2 or older***, you should wear a mask in indoor public places.\n~  In general, you do not need to ***wear a mask*** in outdoor settings.\n~ In areas with ***high numbers of COVID-19 cases***, consider wearing a mask in crowded outdoor settings and for activities with close contact with others who are not fully vaccinated.\n~ People who have a condition or are taking medications that weaken their immune system may not be fully protected even if they are fully vaccinated. They should continue to take all ***precautions recommended*** for unvaccinated people, including ***wearing a well-fitted mask***, until advised otherwise by their healthcare provider.\n~ If you are fully vaccinated, to maximize protection from the Delta variant and prevent possibly spreading it to others, wear a mask indoors in public if you are in an area of substantial or high transmission.",thumbnail="https://cdn-icons-png.flaticon.com/128/4336/4336952.png",color="68, 52,235"))
  
  await ctx.send(embed=op.make_emb(title="**Stay 6 feet away from others**",des="***Inside your home***:\n Avoid close contact with people who are sick.\n~\t\tIf possible, ***maintain 6 feet*** between the person who is sick and other household members.\n***Outside your home***:\n ~ Put ***6 feet*** of distance between yourself and people who don’t live in your household.\n***Remember*** that some people ***without symptoms*** may be able to spread virus.\n~ Stay at least 6 feet (about 2 arm lengths) from other people.\n~ ***Keeping distance from others is especially important for people who are at higher risk of getting very sick***.",thumbnail="https://cdn-icons-png.flaticon.com/128/3579/3579749.png",color="68, 52,235"))

  await ctx.send(embed=op.make_emb(title="**Wash your hands often**",des="Wash your hands often with ***soap and water*** for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing.\n\n***It’s especially important to wash***:\n~   ***Before*** eating or preparing food\n~   ***Before*** touching your face\n~   ***After*** using the restroom\n~   ***After*** leaving a public place\n~   ***After*** blowing your nose, coughing, or sneezing\n~   ***After*** handling your mask\n~   ***After*** caring for someone sick\n~   ***After*** touching animals or pets\n\nIf soap and water are not readily available, ***use a hand sanitizer*** that contains at least ***60% alcohol***. Cover all surfaces of your hands and rub them together until they feel dry.\n***Avoid touching*** your eyes, nose, and mouth with unwashed hands.",thumbnail="https://cdn-icons-png.flaticon.com/128/3027/3027904.png",color="68, 52,235"))
  
  await ctx.send(embed=op.make_emb(title="**Avoid crowds and poorly ventilated spaces**",des="~ Being in crowds like in ***restaurants, bars, fitness centers*** or movie ***theaters*** puts you at higher risk for COVID-19.\n~ Avoid indoor spaces that ***do not offer fresh air from the outdoors*** as much as possible.\n~ If indoors, bring in fresh air by ***opening windows and doors***, if possible.",thumbnail="https://cdn-icons-png.flaticon.com/128/4199/4199272.png",color="68, 52,235"))
  embed=discord.Embed(title="**Helpline numbers**",description="[**Click here**](https://covid19jagratha.kerala.nic.in/resources/downloads/helpline.pdf)",colour=discord.Color.from_rgb(68, 52, 235))
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/2840/2840033.png")
  await ctx.send(embed=embed)


@client.command()#random quotes
async def random(ctx):
  response = requests.get("https://zenquotes.io/api/random")
  random_quote=json.loads(response.text)
  quote = random_quote[0]['q']
  writer=random_quote[0]['a']
  embed = discord.Embed(
      colour = discord.Colour.blue()
  )
  embed.add_field(name=writer,value=quote)
  embed.set_footer(text="Randomly selcted Quote")
  embed.set_thumbnail(url="https://t4.ftcdn.net/jpg/04/16/20/93/240_F_416209306_JCAjOqf28ewGyPl7YjiomN39zIHJD2gN.jpg")
  await ctx.send(embed = embed)




@client.command()#Daily quotes
async def quote(ctx):
  response = requests.get("https://zenquotes.io/api/today")
  random_quote=json.loads(response.text)
  quote = random_quote[0]['q']
  writer=random_quote[0]['a']
  embed = discord.Embed(
        colour = discord.Colour.from_rgb(124, 252, 0)
    )
  embed.add_field(name=writer,value=quote)
  embed.set_footer(text="Quote of the day")
  embed.set_thumbnail(url="https://t4.ftcdn.net/jpg/04/16/20/93/240_F_416209306_JCAjOqf28ewGyPl7YjiomN39zIHJD2gN.jpg")
  await ctx.send(embed = embed)



@client.command()#Basic Appreciating members
async def clap(ctx , name):
  embed=discord.Embed(
    description="Good Job, {}..".format(name),
    colour=discord.Colour.from_rgb(127, 255, 0))
  embed.set_thumbnail(url="https://image.flaticon.com/icons/png/128/5170/5170239.png")
  await ctx.send(embed=embed)

@client.command() #Festive wishes
async def wish(ctx,occasion):
  print(ctx.author.mention)
  if  ctx.author.mention=="<@863277681688838144>":#author.avatar_url)
    if occasion.lower() =="onam":
        embed=discord.Embed(
          title="**Happy onam to all of you...**",
          description="",
          colour=discord.Colour.from_rgb(124, 252, 0)
          )
        embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/5277/5277366.png")
        embed.set_image(url="https://t3.ftcdn.net/jpg/02/74/04/68/240_F_274046850_GoS7i4ZgpJfY5dtrW0PnHPX15Jrzp6Rw.jpg")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif occasion.lower() == "christmas":
        embed=discord.Embed(
          title="**Merry Christmas...**",
          description="",
          colour=discord.Colour.from_rgb(210, 0, 0)
          )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3697/3697198.png")
        embed.set_image(url="https://t4.ftcdn.net/jpg/03/03/83/93/240_F_303839380_Tvazh3GLTs34NQUhISsZVVohBwd794UT.jpg")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif occasion.lower() == "new_year":
        embed=discord.Embed(
          title="**Happy new year...**",
          description="",
          colour=discord.Colour.from_rgb(240, 248, 255)
          )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3918/3918231.png")
        embed.set_image(url="https://t4.ftcdn.net/jpg/01/83/85/35/240_F_183853595_FIYFYiJ5bF8xdZDzLt4yCksVpvtdo5at.jpg")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif occasion.lower() == "diwali":
        embed=discord.Embed(
          title="**Happy Diwali...**",
          description="",
          colour=discord.Colour.from_rgb(255,69,0)
          )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3571/3571472.png")
        embed.set_image(url="https://img.freepik.com/free-vector/cultural-happy-diwali-festival-celebration-background_1055-9360.jpg?size=626&ext=jpg")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:await ctx.message.delete()
  else:
    await ctx.send("**NICE TRY**.")


@client.command()#calculator
async def operate(ctx,problem):
  if problem == "help":
    embed=discord.Embed(title="Operators available are:",description="**Addition `::` +\nSubtraction `::` -\nmultiplication `::` *\nDivision `::` /\nModulus `::` %**",colour=discord.Color.from_rgb(240, 248, 255))
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3820/3820259.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    return
  emb_value=op.operate(problem)
  
  embed=discord.Embed(
    description=f"Requested user is {format(ctx.author.mention)}",
    colour=discord.Colour.from_rgb(0, 255, 255))
  embed.add_field(name="Final result",value=emb_value)
  if emb_value=="Wrong Command":url="https://cdn-icons-png.flaticon.com/128/4085/4085218.png"
  else:url="https://cdn-icons-png.flaticon.com/128/3771/3771278.png"
  embed.set_thumbnail(url=url)
  await ctx.send(embed=embed)


@client.command()#login links
async def log(ctx ,login):
  if login.lower() =="help":
    embed=discord.Embed(title="**Available websites are:**",description="**``instagram\nfacebook\nwhatsapp\nspotify \nrepl \nw3_school \nfreecode_camp \ngmail \ngoogle_search \nplay_store \nnews \nmaps \nyoutube \ntwitter \nroblox \nwikipedia \ndiscord \nflipkart \namazon \nteachmint \nofb``**",colour=discord.Color.from_rgb(240, 248, 255))
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/128/3820/3820259.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    return
  try:
    logs={"instagram":"https://www.instagram.com/",
    "facebook":"https://www.facebook.com/",
    "whatsapp":"https://web.whatsapp.com/",
    "spotify":"https://open.spotify.com/",
    "repl":"https://replit.com/login",
    "w3_school":"https://www.w3schools.com/",
    "freecode_camp":"https://www.freecodecamp.org/",
    "gmail":"https://www.google.com/gmail/",
    "google_search":"https://www.google.co.in/webhp?tab=ww",
    "play_store":"https://play.google.com/store",
    "news":"https://news.google.com/",
    "maps":"https://www.google.co.in/maps",
    "youtube":"https://www.youtube.com/",
    "roblox":"https://www.roblox.com/NewLogin",
    "discord":"https://discord.com/",
    "twitter":"https://twitter.com/",
    "wikipedia":"https://www.wikipedia.org/",
    "flipkart":"https://www.flipkart.com/",
    "amazon":"https://www.amazon.com/",
    "yahoo":"https://in.yahoo.com/",
    "xbox":"https://www.xbox.com/en-IN/",
    "teachmint":"https://www.teachmint.com/",
    "ofb":"https://ofb.academy/",
    "docs":"https://docs.google.com/document/u/0/"}
    if login=="ofb":
      login_1=login.upper()
    else:
      login_1=login.capitalize()
    embed=discord.Embed(description=f"**click [{login_1}]({logs[login]}) to visit Website**",colour=discord.Color.from_rgb(0, 255, 255))
    await ctx.send(embed=embed)
    await ctx.message.delete()
  except:
    embed=discord.Embed(title="**Error occured**",description="***Keyword error***\nTry typing ``/log help`` and try available website....",colour=discord.Color.red())
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()#About Bot command
async def About(ctx):
    embed = discord.Embed(
      Title="About {}".format(client.user),
      description = "Hi everyone .I am a Luna.\nHere are some commands which i will react to ...."
      ,colour = discord.Colour.from_rgb(240, 248, 255)
    )
    embed.set_author(name="{}".format(client.user),icon_url="https://cdn-icons-png.flaticon.com/128/3799/3799933.png")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/256/4762/4762131.png")
  #  embed.set_image(url='https://image.flaticon.com/icons/png/128/5361/5361028.png')
    embed.add_field(name="**/space**", value="Give you ***Astronomy Picture of the Day***``. ",inline=False)
    embed.add_field(name='**/random**',value='I will give you random quotes...',inline=False)
    embed.add_field(name='**/quote**',value='I will give you quote of the day...',inline=False)
    embed.add_field(name='**/find** ``<word>``',value='i will give you meaning any more details about the word\ntype ``/find help!`` for more info',inline=False)
    embed.add_field(name="**/clap** ``<name>``",value="type in a name in the place of ``<name>`` to thank him",inline=False)
    embed.add_field(name="**/operate** ``<num><operator><num>``",value="Helps you in Maths PROBLEM!\n type ``/operate help for the format and available operations``",inline=False)
    embed.add_field(name="**/covid_ins**",value="Gives you a guide ***to prevent Covid-19*** ",inline=False)
    embed.add_field(name="**/log``<name>``**", value="Gives you links of popular websites added to bot \nfor example type whatsapp in the place of <name>\ntype **``/log help``** for more info",inline=False)
    
    await ctx.send(embed = embed)

'''    embed = discord.Embed(
      Title="About {}".format(client.user),
      description = "More Commands coming soon....."
      ,colour = discord.Colour.from_rgb(240, 248, 255))
    embed.set_thumbnail(url="https://image.flaticon.com/icons/png/128/5360/5360797.png")
    await ctx.send(embed=embed)'''


keep_alive()
client.run(os.getenv('Token'))