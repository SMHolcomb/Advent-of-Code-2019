## Advent of Code 
# --- Day 2: 1202 Program Alarm ---

# --- Part ONE ---
# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
# To run one, start by looking at the first integer (called position 0). 
# Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what 
# to do; for example, 99 means that the program is finished and should immediately 
# halt. Encountering an unknown opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a 
# third position. The three integers immediately after the opcode tell you these three 
# positions - the first two indicate the positions from which you should read the 
# input values, and the third indicates the position at which the output should be stored.


# --- Part TWO ---
# The inputs should still be provided to the program by replacing the values at 
# addresses 1 and 2, just like before. In this program, the value placed in address 1 is 
# called the noun, and the value placed in address 2 is called the verb. Each of the two 
# input values will be between 0 and 99, inclusive.

# Once the program has halted, its output is available at address 0, also just like before. 
# Each time you try a pair of inputs, make sure you first reset the computer's memory to 
# the values in the program (your puzzle input) - in other words, don't reuse memory from 
# a previous attempt.

# Find the input noun and verb that cause the program to produce the output 19690720. What 
# is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)


import math
import copy

def getdata(filename, listname):

	file = open(filename,'r')
	for line in file.readlines():
		line = line.split(',')
		for value in line:
			value = int(value)
			listname.append(value)

def process_intcode(data):
	i = 0
	while True: #i = 0

		if data[i] ==1:
			data[data[i+3]] = data[data[i+1]] + data[data[i+2]]

		elif data[i] == 2:
			data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

		elif data[i] == 99:
			break

		i += 4

	#return data


def main():

	# PART I
	data=[]
	getdata("input_day02.txt", data)
	
	# #replace position 1 with value 12 and replace position 2 with value 2
	data[1] = 12
	data[2] = 2

	process_intcode(data)
	print("Part I:" , data[0])
	# # 3101844


	# PART 2

	data=[]
	data_master=[]	# master data used to reset at each loop
	getdata("input_day02.txt", data_master)
	

	# keep running program with various values between 0 and 99 at 0 and 1 positions until ending value at pos. 0 = 19690720
	
	for noun in range(0,100):
		for verb in range(0,100):
			#print("noun", noun, "verb", verb)
			data = copy.deepcopy(data_master)
			
			data[1] = noun 
			data[2] = verb

			process_intcode(data)

			if(data[0] == 19690720):
				#print("data[0]", data[0])
				print("\nPart II:")
				print("noun", noun, "verb", verb)
				print("Final Answer:",100*noun+verb,'\n')

				# 8478

if __name__ == '__main__':
	main()