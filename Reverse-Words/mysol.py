from sys import argv

infile = argv[1]
outfile = argv[2]

with open(infile,'r') as f:
	with open(outfile, "w") as outfile:

		numoflines = f.readline().rstrip('\n')

		for i in range(int(numoflines)):
			sentance = f.readline().split()
			outfile.write(''.join(['Case #',str(i+1),': ']))
			outfile.write(' '.join(sentance[::-1]))
			outfile.write('\n')
