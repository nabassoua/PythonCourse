# max of 3 numbers

a1 = int(input("enter a number: "))
b1 = int(input("enter a number: "))
c1 = int(input("enter a number: "))

def max(a,b,c):

    if a < b:
        if c < a:
            return a * a + b * b
        else:
            return b * b + c * c
    else:
        if c < b:
            return a * a + b * b
        else:
            return a * a + c * c
       
            
result = max(a1, b1, c1)

print("The sum of the 2 largest numbers between {:d}, {:d}, and {:d} is {:d}".format(a1,b1,c1,result))
