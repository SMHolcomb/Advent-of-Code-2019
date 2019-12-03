## Advent of Code 
# --- Day 3: Crossed Wires ---

# --- Part ONE ---


# --- Part TWO ---



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
	# data=[]
	# getdata("input_day02.txt", data)
	
	# #replace position 1 with value 12 and replace position 2 with value 2
	# data[1] = 12
	# data[2] = 2

	# process_intcode(data)
	# print(data[0])
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
				print("data[0]", data[0])
				print("noun", noun, "verb", verb)
				print("final",100*noun+verb)



if __name__ == '__main__':
	main()