"""
#1
N = int(input())
x = 1
while x <= N:
    y = (x ** 2)
    if y <= N:
        print(y)
        x += 1
    else:
        break

#2
n = int(input())
factors = []
x = n
while x > 1:
    if n % x == 0:
        factors.append(x)
    x -= 1
factors.sort()
print(factors[0])

#3
N = int(input())
sum = 1
count = 0
while sum <= N:
    temp = sum
    sum *= 2
    if sum > N:
        sum = temp
        break
    count += 1
print(count, sum)

#4
x = int(input())
y = int(input())
count = 1
while x < y:
    count += 1
    x = x * 1.1
print(count)

#5
inp = True
count = 0
while inp:
    number = int(input())
    count += 1
    if number == 0:
        count -= 1
        break
print(count)

#6
inp = True
count = 0
sum = 0
while inp:
    number = int(input())
    count += 1
    sum += number
    if number == 0:
        count -= 1
        sum -= number
        break
print(sum)

#7
inp = True
count = 0
sum = 0
while inp:
    number = int(input())
    count += 1
    sum += number
    if number == 0:
        count -= 1
        sum -= number
        break
print(sum/count)

#8
inp = True
count = 0
max = 0
while inp:
    number = int(input())
    count += 1
    if number > max:
        max = number
    if number == 0:
        count -= 1
        break
print(max)

#9
number = int(input())
current_index = 0
max_index = 0
max_num = 0
array = []

array.append(number)
while number != 0:
    number = int(input())
    array.append(number)
del(array[-1])


length = len(array)

while current_index < length:
    if array[current_index] > max_num:
        max_num = array[current_index]
        max_index = current_index
    
    current_index += 1

print(max_index)

#10
count = 0
number = 1
while number != 0:
    number = int(input())
    if number % 2 == 0:
        count += 1
count -= 1
print(count)

#11
number = int(input())
current_index = 0
max_index = 0
max_num = 0
array = []

array.append(number)
while number != 0:
    number = int(input())
    array.append(number)
del(array[-1])


length = len(array)

while current_index < length:
    if array[current_index] > max_num:
        max_num = array[current_index]
        max_index = current_index
    
    current_index += 1

if max_index != 1:
    print(max_index)
else:
    print(2)

#12
number = 1
array = []
while number != 0:
    number = int(input())
    if number != 0:
        array.append(number)
    
array.sort()
print(array[-2])

#13
number = 1
array = []
while number != 0:
    number = int(input())
    if number != 0:
        array.append(number)
    
high = max(array)

count = 0
current_index = 0

while current_index < len(array):
    if array[current_index] == high:
        count += 1
    current_index += 1
    

print(count)

#14
n = int(input())

if n == 0:
    fibonacci = 0
elif n == 1:
    fibonacci = 1

a, b = 0, 1
count = 2

while count <= n:
    fibonacci = a + b
    a, b = b, fibonacci
    count += 1

print(fibonacci)

#15
a = int(input())

if a == 0:
    n = 0
elif a == 1 or 2:
    n = 1
"""
#16
list = []
number = int(input())
list.append(number)
same_count = 1
while number != 0:
    number = int(input())
    list.append(number)
list.sort()
del list[0]
print(list)

for _ in list:
    if _ == len(list) - 1:
        break
    if list[_] == list[_+1]:
        special_number = list[_],
    if list[_+1] == special_number:
        same_count += 1
""""""

print(same_count)












