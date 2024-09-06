import math
"""
# 1
first = int(input())
second = int(input())
if first < second:
    print(first)
elif second < first:
    print(second)

#2
number = int(input())
if number > 0:
    print(1)
elif number < 0:
    print(-1)
else:
    print(0)

#3
first = int(input())
second = int(input())
third = int(input())
if first < second and first < third:
    print(first)
elif second < first and second < third:
    print(second)
else:
    print(third)

#4
first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

#5
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())


rowarray = [1, 2, 3, 4, 5, 6, 7, 8]
columnarray = rowarray.copy()

if initialColumn != finalColumn and initialRow != finalRow:
    print("NO")

elif initialColumn == finalColumn and finalRow in rowarray:
    print("Yes")

elif initialRow == finalRow and finalColumn in columnarray:
    print("Yes")

#6
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())


initialCheck = (initialColumn + initialRow) % 2
finalCheck = (finalColumn + finalRow) % 2

if initialCheck == finalCheck:
    print("YES")
else:
    print("NO")

#7
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())

columnDifference = abs(finalColumn - initialColumn)
rowDifference = abs(finalRow - initialRow)

chekSum = abs(columnDifference) + abs(rowDifference)

if chekSum <= 2 and chekSum >= 0:
    print("YES")
else:
    print("NO")

#8
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())

columnMoved = abs(finalColumn - initialColumn)
rowMoved = abs(finalRow - initialRow)

if columnMoved == rowMoved:
    print("YES")
else:
    print("NO")

#9
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())

columnMoved = abs(finalColumn - initialColumn)
rowMoved = abs(finalRow - initialRow)


if columnMoved == rowMoved:
    answer1 = "YES"
else:
    answer1 = "NO"


rowarray = [1, 2, 3, 4, 5, 6, 7, 8]
columnarray = rowarray.copy()

if initialColumn != finalColumn and initialRow != finalRow:
    answer2 = "NO"

elif initialColumn == finalColumn and finalRow in rowarray:
    answer2 = "YES"

elif initialRow == finalRow and finalColumn in columnarray:
    answer2 = "YES"

if answer1 == answer2:
    print(answer1)
elif answer1 == "YES" and answer2 == "NO":
    print(answer1)
elif answer2 == "YES" and answer1 == "NO":
    print(answer2)
else:
    print("NO")

#10
initialColumn = int(input())
initialRow = int(input())
finalColumn = int(input())
finalRow = int(input())

columnDifference = abs(finalColumn - initialColumn)
rowDifference = abs(finalRow - initialRow)

if (columnDifference == 2 and rowDifference == 1) or (columnDifference == 1 and rowDifference == 2):
    print("YES")
else:
    print("NO")

#11
N = int(input())
M = int(input())
K = int(input())

product = N * M

check1 = K % N
check2 = K % M

if (check1 == 0 or check2 == 0) and K < product:
    print("YES")
else:
    print("NO")

#12
year = int(input())

four = year % 4
hundred = year % 100
fourhundred = year % 400

if (four == 0 and hundred != 0) or fourhundred == 0:
    print("LEAP")
else:
    print("COMMON")
"""





























































































































































