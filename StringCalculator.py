def two_numb_add(a):
  sum = 0
  for i in a:
    if i < 1000:
      sum+=i
  return sum

def delimit(x):
  if x[:2] == "\\":
    a = x.split(x[3])
    return a[5:]
  a = x.split(",")
  return a
  
def add(x):
  if x=="" or x=="0":
    return 0
  a = delimit(x)
  
  sum = two_numb_add(a)
  return sum
