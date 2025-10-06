han = open('mbox-short.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()
#Guardian Pattern a bit stronger
  # if len(wds) < 3:
  #   continue
  # if wds[0] != 'From':
  #   continue
  # print(wds[2])

#Guadian Patern with or statement(in a compound statement)
  if len(wds) < 3 or wds[0] != 'From': #Short Circuit Evaluation (Guardian comes first)
    continue
  print(wds[2])