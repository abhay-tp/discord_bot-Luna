import discord
import math
def add_(a):return a+".0"
def operate(pr):
  try:
    if "pow" in pr:
      x=pr.rpartition("pow")
      print(x)
      num_1,num_2=int(x[0]),int(x[2])
      powe=pow(num_1,num_2)
      final=f"{num_1} raised to {num_2} is {powe}"
      return final

    elif "sqrt" in pr:
      x= pr.rpartition("sqrt")
      num=x[2]
      sqrt=math.sqrt(int(num))
      final=f"sqaure root of {num} is {sqrt}"
      return final

    elif "+" in pr.rpartition("+"):
      x=pr.rpartition("+")
      num_1,operator,num_2=x[0],x[1],x[2]
      num_1,num_2=int(num_1),int(num_2)
      sum=num_1+num_2
      final="{} {} {}={}".format(num_1,operator,num_2,sum)
      return final
    elif"-" in pr.rpartition("-") :
      x=pr.rpartition("-")
      num_1,operator,num_2=x[0],x[1],x[2]

      num_1,num_2=int(num_1),int(num_2)
      diff=num_1-num_2
      final="{} {} {}={}".format(num_1,operator,num_2,diff)
      return final
    elif"%" in pr.rpartition("%") :
      x=pr.rpartition("%")
      num_1,operator,num_2=x[0],x[1],x[2]
      num_1,num_2=int(num_1),int(num_2)
      mod=num_1%num_2
      final="{} {} {}={}".format(num_1,operator,num_2,mod)
      return final
    elif"/" in pr.rpartition("/") :
      x=pr.rpartition("/")
      num_1,operator,num_2=x[0],x[1],x[2]
      if num_1.isdecimal==False:num_1=add_(num_1)
      if num_2.isdecimal==False:num_2=add_(num_2)
      num_1,num_2=float(num_1),float(num_2)
      divide=num_1/num_2

      final="{} {} {}={}".format(num_1,operator,num_2,(divide))
      return final
    elif"*" in pr.rpartition("*") :
      x=pr.rpartition("*")
      num_1,operator,num_2=x[0],x[1],x[2]
      num_1,num_2=int(num_1),int(num_2)
      multiple=num_1*num_2
      final="{} {} {}={}".format(num_1,operator,num_2,multiple)
      return final
    else:
      return "Wrong Command"
  except:
      return 



def make_emb(title,des,thumbnail,color):
  embed=discord.Embed(
    title=title,
    description=des, colour=discord.Color.from_rgb(int(color.split(",")[0]),int(color.split(",")[1]),int(color.split(",")[2])))
  embed.set_thumbnail(url=thumbnail)
  return embed



