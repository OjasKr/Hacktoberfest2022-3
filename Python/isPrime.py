a=int(input("Enter a Number - "))
b=0
for i in range(1,a+1):
  if(a%i==0):
    b+=1
if(b==2):
  print("The Number is a Prime Number.")
else:
	print("The Number is not a Prime Number.")
