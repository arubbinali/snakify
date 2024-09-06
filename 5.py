#1
"""
x = input()
print(x[2])
print(x[-2])
print(x[:5])
print(x[:-2])
print(x[::2])
print(x[1::2])
print(x[::-1])
print(x[-1::-2])
print(len(x))

#2
x = input()
c = x.count(" ")
print(c + 1)

#3
x = input()                 
l = len(x)
state = l % 2
y = int(l/2)
yplusone = int(y + 1)
if state == 0:
    first_part = x[y:l]
    second_part = x[:y]
    print(first_part + second_part)
else:
    m = x[y] 
    p = x.replace(m,"", 1)
    first_part = p[y:l]
    second_part = p[:y]
    print(first_part , second_part , m)
   
#4
x = input()
space = x.find(" ")
first = x[:space]
second = x[space + 1:]
print(second, first)

#5
x = input()
one = x.find("f")
two = x.rfind("f")
if one == -1 and two == -1:
    print()
elif one == two:
    print(one)
else:
    print(one, two)

#6
x = input()
c = x.count("f")
if c >= 2:
    one = x.find("f")
    two = x.find("f", one + 1)
    print(one, two)
elif c == 1:
    print(-1)
else:
    print(-2)
    #7

#7
x = input()
one = x.find("h")
two = x.rfind("h")
print(one, two)
print(x.replace(x[one:two + 1], ""))

#8
x = input()
one = x.find("h") + 1
two = x.rfind("h")
first = x[:one]
second = x[two:]
rev = x[one:two]
opp = rev[::-1]
print(first + opp + second)

#9
x = input()
print(x.replace("1", "one"))

#10
x = input()
print(x.replace("@", ""))

#11
x = input()
one = x.find("h") + 1
two = x.rfind("h")
y = x[one:two]
print(x[:one] + y.replace("h", "H") + x[two - 1:])

#12
x = input()
num = len(x)
for x in range(num):
    if x % 3 == 0:
        x.replace(x[], "")

print(x)
"""

# PROGRAM 12 NOT DONE!






































