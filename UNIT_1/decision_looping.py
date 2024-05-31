n=int(input("Enter Number of terms to be checked for odd and even: "))
for i in range(1,n+1):
  if i % 2 == 0:
    print(f"{i}is even")
  else:
    print(f"{i}is odd")
