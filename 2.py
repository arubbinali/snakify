import math
"""
#1
num = int(input())
answer = num - ((num//10) * 10)
print(answer)

#2
number = int(input())
x =((number // 10))
tens = x - ((x // 10) * 10)
print(tens)

#3

number = int(input())
    #ones
ones = number - ((number//10) * 10)
    #tens
x =((number // 10))
tens = x - ((x // 10) * 10)
    #hundreds
y =((number // 100))
hundreds = y - ((y // 10) * 10)

    #Sum
sum = ones + tens + hundreds
print(sum)

#4
number = float(input())
answer = number - int(number)
print(answer)

#5
number = float(input())
x = int(10 * (number - int(number)))
print(x)

#6
N = int(input())
M = int(input())

days = M/N
print(math.ceil(days))

#7
N = int(input())
hours = N // 60
minutes = N % 60
print(hours, minutes)

#8
A = int(input())
B = int(input())
N = int(input())

sum = (A * 100) + B
cost = sum * N
dollars = cost // 100
cents = cost % 100
print(dollars, cents)

#9
H = int(input())
M = int(input())
S = int(input())

convertToHours = H + M / 60 + S / 3600
degrees = convertToHours * 30

print(degrees)


#10
hneedle = float(input())
y = hneedle % 30
x = (y * 360) / 30 
print(x)
"""


























