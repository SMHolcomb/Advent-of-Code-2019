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

def main():
	passwords = []
	# Part I
	count=0
	for i in range(359282,820402):
		i+=1
		stri = str(i)
		if( (stri[0]==stri[1])  or (stri[1]==stri[2]) or (stri[2]==stri[3]) or (stri[3]==stri[4]) or (stri[4]==stri[5]) ):
				
			if ( (int(stri[0])<=int(stri[1])) and (int(stri[1])<=int(stri[2])) and (int(stri[2])<=int(stri[3])) and (int(stri[3])<=int(stri[4])) and (int(stri[4])<=int(stri[5])) ) :
			
				count+=1
				passwords.append(i)
				
	print(count)
	# 511

	# Part II

	#print(len(passwords))
	count2=0
	wrong=[]
	for num in passwords:

		# or num in range(0,2):
		flg=True  #assume it meets criteria
	
		stri=str(num)
		#print(stri)
		for j in range(0,len(stri)-3):
			#if there are 2 in a row, but not three then we're ok no matter what else is in the rest of the number
			if ( ( int(stri[j]) == int(stri[j+1]) )  and ( int(stri[j]) == int(stri[j+2]) )  ):
				flg=False
				print(stri,"no")
				break
			
		
			elif ( ( int(stri[j]) == int(stri[j+1]) )  and ( int(stri[j]) != int(stri[j+2]) )  ):
					
				print(stri,"yes")	
		if flg:
			count2+=1
		else:
			wrong.append(num)

	print(count2)
	# for num in wrong:
	# 	print(num)

	#404 -- WRONG TOO HIGH
	#290 -- TOO LOW
	#221 -- TOO LOW
	#370 -- WRONG BUT NO DETAIL ON HIGH / LOW
	#355 -- WRONG BUT NO DETAIL ON HIGH / LOW
	#369 -- WRONG BUT NO DETAIL ON HIGH / LOW


if __name__ == '__main__':
	main()