
t = int(input())

for i in range(1, t + 1):
  F, S = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  #print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
  seats = {}
  for j in range(1,F+1):
    n,m = [int(s) for s in input().split(" ")]
    if n not in seats:
        seats[n] = set()
    if m not in seats:
        seats[m] = set()
    seats[n].add(m)
    seats[m].add(n)

  print("Case #{}: {}".format(i, max([len(v) for k,v in seats.items()])))
  # print(max([len(v) for k,v in seats.items()]))
