## Advent of Code 
# --- Day 1: The Tyranny of the Rocket Equation ---

# --- Part ONE ---
# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
# They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass
# , divide by three, round down, and subtract 2.

# --- Part TWO ---

# Fuel itself requires fuel just like a module - take its mass, divide by three
# , round down, and subtract 2. However, that fuel also requires fuel, and that 
# fuel requires fuel, and so on. Any mass that would require negative fuel should 
# instead be treated as if it requires zero fuel; the remaining mass, if any, 
# is instead handled by wishing really hard, which has no mass and is outside 
# the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total. Then, 
# treat the fuel amount you just calculated as the input mass and repeat the 
# process, continuing until a fuel requirement is zero or negative. For example:


import math

def getdata(filename, listname):
	with open(filename,'r') as infile:
		for value in infile:
			listname.append(int(value))

def get_fuel_1(mass):
	fuel = math.floor(mass/3) - 2
	return fuel

def get_fuel_2(mass):
	fuel = 0 

	while (math.floor(mass/3) - 2)  >= 0:
		mass = math.floor(mass/3) - 2
		fuel += mass

	return fuel


def main():

	data=[]
	getdata("input_day01.txt", data)

	#print(get_fuel_2(14))
	#print(get_fuel_2(1969))

	fuel_1 = sum([get_fuel_1(x) for x in data])
	print(fuel_1)
	# 3360301

	fuel_2 = sum([get_fuel_2(x) for x in data])
	print(fuel_2)
	#5037595

if __name__ == '__main__':
	main()