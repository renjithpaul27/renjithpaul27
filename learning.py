

def list_common(a,b):
  c=[]
  for each_a in a:
    if each_a not in b:
      c.append(each_a)
  print(c)



if __name__ == "__main__":
  list_common([1,2,3],[4,5,6,1])