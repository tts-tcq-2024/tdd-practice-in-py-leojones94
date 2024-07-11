def numb_add(a):
  sum = 0
  for i in a:
    if int(i) <= 1000:
      sum+=int(i)
  return sum

def negaterror(neg,a):
  if len(neg)>1:
    NegError=ValueError("negatives not allowed " + neg)
    raise NegError
  return a

def numbcheck(a):
  neg=""
  for i in a:
    if int(i)<0:
      neg+=(i+" ")
  return(negaterror(neg,a))

def newline(x):
  b = x.split("\n")
  for j in b:
    if "," in j:
      b.extend(j.split(","))
      b.remove(j)
  return (b)

def delimit(x):
  if x[:2] == "//":
    a = x[4:].split(x[2])
    return a
  return (newline(x))
  
def add(x):
  if x=="" or x=="0":
    return 0
  a = delimit(x)
  a = numbcheck(a)
  sum = numb_add(a)
  return sum
