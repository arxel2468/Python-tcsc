f=open('6sample.txt','r')
t=f.readlines()
print(t[-1])
f.close

# def LastLines(f,N):
#     with open(f) as file:
#         print("Last 'n' lines from test : ",f)
#         for line in (file.readlines() [-N:]):
#             print(line,end='')

# name=input("Enter name of the file: ")
# N=int(input("NO. of the last lines to read: "))
# try:
#     LastLines(name,N)
# except:
#     print('File Not Found')