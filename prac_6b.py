f=open('sample.txt','a+')
f.write('\nPython\n')
f=open('sample.txt','r')
t=f.read()
print (t)
f.close