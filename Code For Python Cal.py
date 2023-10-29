# Very Basic Python Code To make A calculator #
a=int(input("Enter Any Number:-"))
b=int(input("Enter Any Number:-"))
c=input("Enter any function +,-,*,%,/,// ----->")

if c=="+":
 print(a+b)

elif c=="-":
 print(a-b)

elif c=="*":
 print(a*b)

elif c=="%":
 print(a%b)

elif  c=="/":
 print(a/b)

elif c=="//":
 print(a//b)

else:
  print("You Have Entered An Invalid Function Try +,-,*,%,/,//")
