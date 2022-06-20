# from array import *
# vals =array('i',[5,9,4,2])
# print (vals)

     #Reverse

# from array import *
# vals =array('i',[5,9,4,2])
# vals.reverse()
# print (vals)


     #old array in new array

from array import *
vals =array('i',[5,9,4,2])
newArr = array(vals.typecode,(#a 
 a*a for a in vals))

for e in newArr:
   print (e)