import os

class Cell():
  def __init__(self,name,adress,count,n):
    self.name=name
    self.count=count
    self.n=n
    self.adress=adress
    self.newname=self.name+"1"
    t1="from pyforchange.cell import *\n"
    t2=self.newname+"=Cell(\""+self.newname+"\",\""+adress+"\","+str(self.count+1)+","+str(n)+")\n"
    t3="if "+self.newname+".count>="+str(n)+":\n"
    t4="\tclearall("+str(n)+","+self.newname+".adress)\n"
    t5="else:\n"
    t6="\t"+self.newname+".reproduction()\n"
    t7="\texecute("+self.newname+".newname)\n"
    self.text=t1+t2+t3+t4+t5+t6+t7
    print(adress+" #"+str(self.count)+" was added succesfully")
  def reproduction(self):
    f=open(self.newname+".py",'w')
    f.write(self.text)
    f.close()

def execute(name):
  try:
    t="/usr/bin/python "+name+".py"
    os.system(t)
  except:
    print("Execute error in: "+"/usr/bin/python "+name+".py")

def clearall(n,name):
  t=""
  for i in range(1,n+1):
    t+="1"
    try:
      os.remove(name+t+".py")
      print(name+" #"+str(i)+" was removed succesfully")
    except:
      print(name+" #"+str(i)+" was not removed")
