def fibonacci (n):
   if n == 0 or n==1:
    return (1)
   else:
    return(fibonacci(n-1) + fibonacci(n-2))
  

def lucas(n):
  if n== 0:
    return (2)
  if n== 1:
    return(1)
  else:
    return(lucas(n-1) + lucas(n-2))

  
def sum(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum(n-1, first, second) + sum(n-2, first, second)

 