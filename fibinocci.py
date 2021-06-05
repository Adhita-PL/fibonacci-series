nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nx = n1 + n2
       # update values
       n1 = n2
       n2 = nx
       count += 1 