# -*- coding: utf-8 -*-
"""Final Assessment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bz5vNbMElOytgX_SjKWsRDP8LJG4JDrK

### PERFECT NUMBER
"""

n = int(input("Enter a number"))
sum = 0
for i in range(1,n):
  if n%i==0:
    sum+=i
print("sum=",sum)
if(sum==n):
  print("Perfect number")
else:
  print("Not a perfect number")

