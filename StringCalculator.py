def two_numb_add(a):
  sum = 0
  for i in a:
    if int(i) < 1000:
      sum+=int(i)
  return sum

def delimit(x):
  if x[:2] == "//":
    a = x[4:].split(x[2])
    return a
  a = x.split(",")
  return a
  
def add(x):
  if x=="" or x=="0":
    return 0
  a = delimit(x)
  sum = two_numb_add(a)
  return sum
