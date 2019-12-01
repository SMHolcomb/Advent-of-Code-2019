## Advent of Code 
# --- Day 1: The Tyranny of the Rocket Equation ---

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
# They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass
# , divide by three, round down, and subtract 2.
import math

def getdata(filename, listname):
	# import frequency file
	with open(filename,'r') as infile:
		for value in infile:
			listname.append(int(value))


def get_fuel(mass):
	fuel = math.floor(mass/3) - 2
	return fuel


def main():

	data=[]
	getdata("input_day01.txt", data)

	fuel = sum([get_fuel(x) for x in data])
	print(fuel)
	# 3360301


if __name__ == '__main__':
	main()