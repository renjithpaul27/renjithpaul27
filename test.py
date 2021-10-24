import sys

def sum_array(lis):
  s=0
  for each in lis:
    s = each + s
  print(s)

def factorial(n):
  if n < 0:
    return 0 
  elif n == 1:
    return 1
  else:
    fact = 1
    while n>1:
      fact = n*fact
      n -=1
    return fact

def largest(a):
  largest = 0
  for each in a: 
    if each > largest:
      largest = each 
  print(largest)


def rotate_string(a):
  rev =''
  for each in a:
    rev =  each + rev
  print(rev)

def rotate_string_list_slice(a):
  rev = a[::-1]
  print(rev)

def sum_list(a,b):
  indx = 0
  sm = []
  for each in a:
    sm.append(each+b[indx])
    indx +=1
    #break 
  print(sm)

def listduplicateremoval(a):
  return list(set(a))

def findindexfirstmatch(a_lis,a_ele):
  ind = -1
  for each in a_lis:
    ind += 1
    if a_ele == each:
      return ind
  return "no record found"

def rotate_list(a):
  rot = []
  len_list = len(a)
  for each in range(0,len_list):
    rot.append(a[len_list-1])
    len_list -= 1
  print(rot)

def sort_list(a):
  sorted = []
  for each in range(0,len(a)):
    min = a[0]
    for each_b in range(0,len(a)):
      if min > a[each_b]:
        min = a[each_b]
    sorted.append(min)
    a.remove(min)
  print(sorted)


def count_of_occ(a):
  occ = {}
  for each_a in a:
    cnt=0
    for each_b in a:
      if each_a == each_b:
        cnt+=1
    occ[each_a]=cnt
  print(occ)

def list_common(a,b):
  dup_removed=[]
  common=[]
  for i in a:
    if i not in dup_removed:
      dup_removed.append(i)
  for each_a in dup_removed:
    for each_b in b:
      if each_a == each_b:
        common.append(each_a)
        break
  print(common)

from functools import reduce
def list_sum_reduce(a):
    return reduce(lambda x,y:x+y,a)    


def remove_negatives(a):
  return list(filter(lambda x:x>0,a))


def sort_list_desc(a):
  sorted = []
  for each in a:
    lar = each
    for each_b in a:
      if each_b > lar:
        lar = each_b
    sorted.append(lar)
    a.remove(lar)
  print(sorted)


def max_list(a):
  maxi = a[0]
  for each in a: 
    if each > maxi:
      maxi = each 
  print(maxi)

def reverse_list(a):
    reversed = []
    len_list = len(a)
    for each in range(0,len_list):
      reversed.append(a[len_list-1])
      len_list -= 1
    print(reversed)

def get_notcommon(a,b):
  notcommon=[]
  dedup_a = list(set(a))
  dedup_b = list(set(b))
  for each_a in dedup_a:
    if each_a not in dedup_b:
      notcommon.append(each_a)
  for each_b in dedup_b:
    if (each_b not in dedup_a) and (each_b not in notcommon):
      notcommon.append(each_b)
  print(notcommon)

def find_duplicates_list(a):
  ind = prev_val = 0
  dup =[]
  for each_a in a:
    ind += 1
    if prev_val == each_a:
      prev_val = each_a
      continue
    prev_val = each_a
    for each_b in range(ind,len(a)):
      if each_a == a[each_b]:
        dup.append(each_a)
        break 
  print(dup)

def anagram(s1,s2):
  if len(s1) != len(s2):
    return "Not anagram"
  if set(s1) == set(s2):
    return "Anagram"
  else: 
    return "not anagram"

def remove_dup_list_set(a):
  b=list(set(a))
  print(b)

def remove_dup_list(a):
  b=[]
  indx=0
  for each in a:
    if each in b:
      pass
    else:
      b.append(each)
  print(b)

def findsumpair(a,num):
  ind = 0
  b=a.copy()
  for each in a:
    ind += 1 
    for each_a in range(ind,len(b)):
      if each + a[each_a] == num:
        print("Found pair : {} , {}".format(each, a[each_a]))
        b.remove(a[each_a])

def check_string_if_reverse_match(s1,s2):
  idx = -1
  if len(s1) != len(s2):
    return 'Not palindrome'
  for each in s1:
    for each_b in range(0,len(s2)):
      if each == s2[idx]:
        idx -= 1
        break
      else:
        return 'Not palindrome'
  return 'Palindrome'

def palindrome(s1):
  ind = -1
  for each in s1:
    for each_b in range(0,len(s1)):
      if each == s1[ind]:
        ind -= 1
        break
      else:
        return "Not palindrome"
  return "palindrome"

def validipaddr(a):
  b=a.split(".")
  if len(b) > 4:
    return 'invalid'
  try:
    for each in b:
      if int(each):
        pass
    return 'valid'
  except:
    return 'Invalid'
    
def sum_lists(a,b): # duplicate of sum_list
  s=[]
  ind=0
  for each in a:
    s.append(a[ind]+b[ind])
    ind += 1
  print(s)

def rotate_lists(a): # duplicate of rotate_list
  rot = []
  len_a = len(a)
  for each in range(0,len_a):
    rot.append(a[len_a-1])
    len_a -= 1
  print(rot)

def anita_reverse_list(a):
  s=0
  for x in a:
      s=s+x
  print(s)
  


  # [4,3,2,1]


if __name__ == "__main__":
  #t=[1,2,3,4]
  #anita_reverse_list(t)
  #a = [1,2,3,4,-1,10,8,7,4]
  #largest(a)
  #sum_array(a)
  #n = input("Enter the string:")
  #print(factorial(int(n)))
  #rotate_string(n)
  #rotate_string_list_slice(list(n))
  #a=[1,2,3]
  #b=[4,5,6]
  #sum_list(a,b)
  #rotate_lists(a)
  #print(listduplicateremoval(a))
  #print(findindexfirstmatch(a,3))
  #rotate_list(a)
  a=[5,3,2,1]
  sort_list(a)
  #count_of_occ(a)
  #a=[1,2,3,4,1,2,3,8,9]
  #b=[3,4,5,6,3,4,5,6]
  #list_common(a,b)
  #print(list_sum_reduce(a))
  #a=[1,2,-3,4,1,-2,3,-8,9]
  #print(remove_negatives(a))
  #sort_list_desc(a)
  #max_list(a)
  #a=['a','b','c','d']
  #reverse_list(a)
  #a=[1,2,3,4]
  #b=[1,2,5,6]
  #get_notcommon(a,b)
  #a=[1,1,2,3,4,4,5,5]
  #find_duplicates_list(a)
  #s1='lottery'
  #s2='yrettdl'
  #print(anagram(s1,s2))
  #a=[1,1,2,3,4,4,5,5]
  #remove_dup_list(a)
  #a=[1,3,2,2,5,6,2,1,3,4,1,2,3]
  #findsumpair(a,4)---check this
  #s1='abc'
  #s2='sbc'
  #print(check_string_if_reverse_match(s1,s2))
  #s1='abbba'
  #print(palindrome(s1))
  #a='1.2.3.4.5'
  #print(validipaddr(a))