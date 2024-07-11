def numb_add(a):
  sum = 0
  for i in a:
    if int(i) < 1000:
      sum+=int(i)
  return sum

def newline(x):
  a=[]
  b = x.split("\n")
  for j in b:
    if "," in j:
      a.append([p for p in (j.split(","))])
    elif "," not in j:
      a.append([j])
  return sum(a,[])

def delimit(x):
  if x[:2] == "//":
    a = x[4:].split(x[2])
    return a
  return (newline(x))
  
  
def add(x):
  if x=="" or x=="0":
    return 0
  a = delimit(x)
  sum = numb_add(a)
  return sum

print(add("1\n2,3"))
