
## Reverse of a string??

s=input("Enter a string: ")
x=''
for i in range(-1,-len(s)-1,-1):
    x+=s[i]
print(x)
