'''
A Fibonacci function is an example of a recursive function,
The function returns the fibonacci number of n belonging to the range of z+ or integer number and zero 
wich mean 'n' between zero and infinety number,
the series is summation of two previous numbers as :
1,1,2,3,5
the function treate with problem by divide it to base case when n ==zero or n==1 
the function return 1  
another case as 'n >1'  the function repeats itself whithout need to use any looping
and this what i mean by "recursive function"
'''

def fibonacci (n):
   if n == 0:
      return 1
   if  n==1:
       return 1
   if n>1:
     return(fibonacci(n-1) + fibonacci(n-2))
'''
another example on recursive function lucas function 
 base cas is n =0 return 2 ; n=1 return 1 else repeat itself by 
 using (lucas(n-1) + lucas(n-2))
 ''' 

def lucas(n):
  if n== 0:
    return (2)
  if n== 1:
    return(1)
  if n>1:
    return(lucas(n-1) + lucas(n-2))
'''
another example on -recursive function is sum function which
 calculates the sum series like Fibonacci-and lucs series for a number.
starting with first and second as the initial values.
The function takes three arguments: 
n represents the index of the number in the sequence to be calculated,
first is the value at index 0, and second is the value at index 1.
The base cases are defined when n is equal to 0 or 1. If n is 0,
the function returns the value of first. If n is 1, it returns the value of second.
For n greater than 1, the function recursively calls itself twice: once with n-1 and once with n-2 as the new values for n. The first and second values are passed along to maintain the initial values. It then returns the sum of the two recursive calls.
'''
  
def sum(n, first=0, second=1):
    if n == 0:
        return first
    if n == 1:
        return second
    if n>1:
        return sum(n-1, first, second) + sum(n-2, first, second)
if __name__=="__main__":
   fibonacci(2)
   lucas(4)
   sum(2,0,1)


