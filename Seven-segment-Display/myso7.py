from sys import argv

infile = argv[1]
outfile = argv[2]

digits_dict = {
	9: int('1111011',2),
	8: int('1111111',2),
	7: int('1110000',2),
	6: int('1011111',2),
	5: int('1011011',2),
	4: int('0110011',2),
	3: int('1111001',2),
	2: int('1101101',2),
	1: int('0110000',2),
	0: int('1111110',2),
}

def display_possible_for_number(display, number, digit_states):
	number_bits = [(number >> bit) & 1 for bit in range(7 - 1, -1, -1)]
	display_bits = [(display >> bit) & 1 for bit in range(7 - 1, -1, -1)]

	# for digit_states: 1=burned out, 2=unknown, 3=functional
	for i in range(7):
		if (digit_states[i] == 1 and display_bits[i] == 1):
			return 'error'
		elif (display_bits[i]==1 and number_bits[i]==0):
			return 'error'
		elif (digit_states[i] ==3 and display_bits[i]==0 and number_bits[i]==1):
			return 'error'
		elif (digit_states[i] == 1 or digit_states[i] ==3):
			continue
		elif (display_bits[i]==0 and number_bits[i]==1):
			digit_states[i] = 1
		elif (display_bits[i]==0 and number_bits[i]==0):
			digit_states[i] = 2
		elif (display_bits[i]==1 and number_bits[i]==1):
			digit_states[i] = 3

	return digit_states

def transform_display_with_error(display, digit_states):
	# turn the error digits off: if state=1, turn off
	number_bits = [(display >> bit) & 1 for bit in range(7 - 1, -1, -1)]
	for i in range(7):
		if (number_bits[i] == 1 and digit_states[i]==1):
			number_bits[i] = 0

	return (''.join(str(x) for x in number_bits))

with open(infile,'r') as f:
	with open(outfile, "w") as outfile:

		numoflines = f.readline().rstrip('\n')

		for i in range(int(numoflines)):
			# for each line
			# read all inputs
			allinput = f.readline().split()

			num_digits = int(allinput[0])
			first_input = int(allinput[1],2)

			dict_states = {}

			for num in range(10):
				digit_states = display_possible_for_number(first_input, digits_dict[num],[2] * 7)
				if digit_states != 'error':
					dict_states[num] = digit_states 

			print dict_states
			ERROR = False
			num_answer = 0

			for number, digit_states in dict_states.iteritems():
				# iterate through the list of input row
				print "number = ", number
				for j in range(2,len(allinput)):
					ERROR=False
					input_number = int(allinput[j],2)
					next_number = number - 1 if (number != 0) else 9
					print "next_number = ", next_number
					print "digit_states = ", digit_states
					ret_digit_states = display_possible_for_number(input_number, digits_dict[next_number], digit_states)
					print "ret_digit_states = ", ret_digit_states
					if ( ret_digit_states == 'error'):
						print "ERROR! go to the next possible number of error"
						ERROR=True
						break
					else:
						digit_states = ret_digit_states
						number = next_number

				if ERROR == False:
					print "we found a match:", number
					num_answer = num_answer + 1

			outfile.write(''.join(['Case #',str(i+1),': ']))
			if num_answer > 1:
				outfile.write("ERROR!")
			else:
				print number
				next_number = number -1 if (number != 0) else 9
				next_display_number = transform_display_with_error(digits_dict[next_number], digit_states)
				outfile.write(next_display_number)
				print "writing to file:", next_display_number

			outfile.write('\n')




