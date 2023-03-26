def myfunc(mystr):
  import string
  alphabet = string.ascii_lowercase
  result = []
  
  for x in mystr:
    index = alphabet.find(x.lower())+1
    if index != 0:
      result.append(str(index))
  return result
l=myfunc("The sunset sets at twelve o clock")
print(l)