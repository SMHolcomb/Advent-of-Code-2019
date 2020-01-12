## Advent of Code 
# --- Day 4: Secure Container ---

# --- Part ONE ---
'''
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves 
had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 359282-820401
'''
# --- Part TWO ---
'''
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''
import itertools

def main():
	passwords = []

	# Part I
	count=0
	for i in range(359282,820402):

		stri = str(i)
		if( (stri[0]==stri[1])  or (stri[1]==stri[2]) or (stri[2]==stri[3]) or (stri[3]==stri[4]) or (stri[4]==stri[5]) ):
				
			if ( (int(stri[0])<=int(stri[1])) and (int(stri[1])<=int(stri[2])) and (int(stri[2])<=int(stri[3])) and (int(stri[3])<=int(stri[4])) and (int(stri[4])<=int(stri[5])) ) :
			
				count+=1
				passwords.append(i)


	print(count)
	# 511


	# Part II
	count=0

	for num in passwords:
		# find maximum length of repeated digits
		lnum = [int(x) for x in str(num)]
		m = [(x[0], len(list(x[1]))) for x in itertools.groupby(lnum) ]
		
		if [item for item in m if item[1]==2]:
			count+=1
	
	print(count)	
	#316

if __name__ == '__main__':
	main()