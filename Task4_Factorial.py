#. Create a Python function to calculate factorial of a number using recursion.



def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    



num=int(input("Enter a number"))
if num<0:
    print("Negative number dosenot have any factorial")
else:
    result=factorial(num)
    print(f"Factorial of given {num} is {result}")


