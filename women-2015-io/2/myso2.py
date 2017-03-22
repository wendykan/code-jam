from sys import argv
import itertools
infile = argv[1]
outfile = argv[2]

with open(infile,'r') as f:
	with open(outfile, "w") as outfile:

		T = int(f.readline().rstrip('\n'))

		for i in range(T):
			K,V = f.readline().split(' ')
			K=int(K)
			V=int(V)
			num_bland = 0

			# generate the set
			col = list(itertools.product(range(K+1),repeat=3))

			for tup in col:
				if (max(tup) - min(tup) <= V):
					num_bland = num_bland + 1



			outfile.write(''.join(['Case #',str(i+1),': ']))
			outfile.write(str(num_bland))
			outfile.write('\n')
