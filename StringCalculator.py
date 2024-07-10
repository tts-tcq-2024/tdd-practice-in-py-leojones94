def add(x):
  if x=="" or x=="0":
    return 0
  else:
    a = x.split(",")
    sum = 0
    for i in a:
      sum += int(i)
    return sum
