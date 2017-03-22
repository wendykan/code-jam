# import itertools
# def generate_groups(lst, n):
#     if not lst:
#       yield []
#     else:
#       for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n-1)):
#         for groups in generate_groups([x for x in lst if x not in group], n):
#           yield [group] + groups


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  probs = [float(s) for s in input().split(" ")]
  probs = sorted(probs)
  # print(probs)  
  prob_success = 1.0
  for j in range(n):
    # print(i,2*n-i-1,probs[i], probs[2*n-i-1])
    prob_success *= (1 - probs[j]*probs[2*n-j-1])


  # cases = list(generate_groups(range(len(probs)),2))

  # best_prob = 0.0
  # for case in cases:
  #   prob_success = 1.0
  #   for pair in case:
  #     prob_success *= (1 - probs[pair[0]]*probs[pair[1]])

  #   if best_prob < prob_success:
  #     best_prob = prob_success
  #   if best_prob == 1.0:
  #     continue

  print("Case #{}: {}".format(i, prob_success))
  # check out .format's specification for more formatting options

