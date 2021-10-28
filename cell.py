import os

def nothing(var):
    return var

class Cell():
	def __init__(self, name, adress, count, n, function = nothing, args = [1], verbose = False):
		self.name = name
		self.adress = adress
		self.count = count
		self.n = n
		self.newname = self.name + "1"
		self.f = function().__str__()

		foo = function()

		t0 = "from cell import *\n"
		t1 = f"from {adress} import {self.f}\n"
		t2 = f"foo = {self.f}()\n" + f"foo.execute({args})\n"
		t3 = f"{self.newname} = Cell(\"{self.newname}\", \"{adress}\", {self.count + 1}, {n}, {foo.__str__()}, {args})\n"
		t4 = f"if {self.newname}.count >= {n}:\n"
		t5 = "\tclearall(" + str(n) + ", " + self.newname + ".adress)\n"
		t6 = "else:\n"
		t7 = "\t" + self.newname + ".reproduction()\n"
		t8 = "\texecute(" + self.newname + ".newname)\n"

		self.text = t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
		
		if verbose:
			print(f"{adress} #{self.count} was added succesfully")
		
	def reproduction(self):
		f = open(self.newname + ".py", 'w')
		f.write(self.text)
		f.close()

path = "py"

def execute(name):
	try:
		t = f"{path} {name}.py"
		os.system(t)
	except:
		print(f"Execute error in: {path} {name}.py")

def clearall(n, name, verbose = False):
	t = ""
	for i in range(1, n + 1):
		t += "1"
		try:
			os.remove(name + t + ".py")
			if verbose:
				print(name + " #" + str(i) + " was removed succesfully")
		except:
			if verbose:
				print(name + " #" + str(i) + " was not removed")
