from sys import argv

infile = argv[1]
outfile = argv[2]

with open(infile,'r') as f:
	with open(outfile, "w") as outfile:

		T = int(f.readline().rstrip('\n'))

		for j in range(T):
			B = int(f.readline().rstrip('\n'))
			line = f.readline()
			line = line.replace("I","1").replace("O","0")
			n=8
			chars = [line[i:i+n] for i in range(0, len(line), n)]


			outfile.write(''.join(['Case #',str(j+1),': ']))
			for k in range(B):
			  outfile.write(str(unichr(int(chars[k],2))))
			outfile.write('\n')
