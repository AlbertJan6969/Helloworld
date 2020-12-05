#today we are discussing the difference between lambda and def.
#Needing no funcition name,lambda is relative simple way to define a function
#lambda = def+return  see the following examples!
c = lambda x,y,z: x*y*z
print(c(2,3,4))
print()
print("Hey")
def F(i,j):
    return (i+j)
print(F(2,1))
# Now about function reduce()  There is not dot after reduce!
#Essencially reduce() function applies only to two variables
print('Hello world')
from functools import reduce
print(reduce(F,[1,5,6]))
print('Hello world')
print(reduce(lambda x,y: x*y, [3,4,5,7] ))#(((3+4)+5)+7) acts two by two
print(reduce(lambda x,y: x+y, range(1,101,2)))
# count the sequence Tn=a,aa, aaa, aaaa
n=int(input('numbers of term'))
a=int(input('digits'))
T=0
Sn=[]#Note this should be put outside the loop otherwise there will
#be only one element in the set because of clearing elements every time
for looper in range(n):
    T = T + a
    a=10*a
    Sn.append(T)
    print(T)
print(reduce(lambda x,y:x+y,Sn))
#count(),str.count(sub, start= 0,end=len(string))
I="Here is to test the number of letters in count function"
print(I.count('i',0,100))
