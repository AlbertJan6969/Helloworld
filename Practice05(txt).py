f = open('woo.txt','a')# w:write r:read a:write but not cover original
print('this is a test:007',file=f)
f.closed# this is important otherwise the next order is will...
print("Hi")#if u don't close the file, it still prints in file
with open('woo.txt',"r")as f:
    print(f.read())
import sys
sys.stdout = open('test.txt','w')
print('Hello world,  Python')
#sys.stdout.write('hello'+'\n')=print('hello')
print("this will appear in file but not in screen")
with open ('C:\Users\Administrator\Desktop\ju1.txt','r') as z:
    print(z.read())



