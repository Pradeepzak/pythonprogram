a=int(input("enter a year:"))
if((a%4==0) or (a%400==0) or (a%100!=0)):
  print('leap year')
else:
  print('not a leap year')
