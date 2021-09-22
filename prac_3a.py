# def panagram(nt):
#       check="abcdefghijklmnopqrstuvwxyz"
#   for l in check:
#     if(l in nt):
#          continue
#     else:
#          return False
#    return True           

# n=input("Enter Any Text:\n")
# if(panagram(n.lower())):
#   print("Yes It is a Pangram")
# else:
#   print("No It is not a Pangram")

import string
def ispangram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=set(str1.lower())
print(ispangram("hello world"))