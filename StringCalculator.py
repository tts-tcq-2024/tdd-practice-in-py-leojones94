def add(x):
  if x=="" or x=="0":
    return 0
  a = x.split(",")
  return int(a[0]) + int(a[1])
