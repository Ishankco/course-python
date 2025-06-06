# by Factorial by using loop
n = int(input("enter a number"))
fact =1
for i in range(1,n+1):
    fact = fact *i

print(fact)

#by using reccursion
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

a=fact(5)
print(a)