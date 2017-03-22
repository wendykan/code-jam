from sys import argv
import math
infile = argv[1]
outfile = argv[2]

# compute digits of factorial skipped with n_excl
def fact_digits(n,n_excl):
	num_digs = 0
	for i in range(1,n+1)[::-n_excl]:
		num_digs = num_digs + math.log10(i)
	return math.ceil(num_digs)


with open(infile,'r') as f:
	with open(outfile, "w") as outfile:

		T = int(f.readline().rstrip('\n'))

		for i in range(T):
			D = int(f.readline())

			N = 9000
			outfile.write(''.join(['Case #',str(i+1),': ']))
			print ''.join(['Case #',str(i+1),': '])
			
			if D <= 4:
				outfile.write("...\n")
				print "..."
				continue

			lower = 1
			upper = N

			#binary search
			while (lower <= upper):
				middle = sum([upper,lower])/2
				return_f_d = fact_digits(N,int(middle))
				if return_f_d < D:
					upper = middle-1
				else:
					lower = middle+1

			outfile.write("IT'S OVER 9000")
			outfile.write('!'*int(lower))

			outfile.write('\n')
