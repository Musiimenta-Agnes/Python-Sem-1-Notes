# THE LOOPS. ( THE FOR LOOPS)
list = ['Apple', 'Banana', 'Cherry']
for x in list:
  print(x) # This returns elements in the list
  



# USE OF THE BREAK STATEMENT(1)
list = ['Apple', 'Banana', 'Cherry']
for x in list:
  print(x)
  if x == 'Banana':
   break # This returns 'apple' and 'Banana' because you print (x) befor breaking from 'banana'.
  


 # USE OF THE BREAK STATEMENT (2)
list = ['Apple', 'Banana', 'Cherry']
for x in list:
  if x == 'Banana':
    break
  print(x) # This returns 'Apple' Only because the break comes befor the print.



  # USE OF THE CONTINUE STATEMNET
  
list = ['Apple', 'Banana', 'Cherry']
for x in list:
  if x == 'Banana':
    continue
  print(x) # This returns 'Apple' and 'Cherry' becoz it eliminates 'Banana'.
