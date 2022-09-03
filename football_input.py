team1 = str(input())
team2 = str(input())
team3 = str(input())
team4 = str(input())
def sum(*x):
    sum1 = 0
    for i in x:
        sum1 += i
    return sum1
#inputgoal
goal1 = []
for i in range(4):
    x = int(input())
    goal1.append(x)
goal1[0] = 0
sum1 = sum(goal1[0],goal1[1],goal1[2],goal1[3])
goal2 = []
for i in range(4):
    x = int(input())
    goal2.append(x)
goal2[1] = 0
sum2 = sum(goal2[0],goal2[1],goal2[2],goal2[3])
goal3 = []
for i in range(4):
    x = int(input())
    goal3.append(x)
goal3[2] = 0
sum3 = sum(goal3[0],goal3[1],goal3[2],goal3[3])
goal4 = []
for i in range(4):
    x = int(input())
    goal4.append(x)
goal4[3] = 0
sum4 = sum(goal4[0],goal4[1],goal4[2],goal4[3])
#point
#12
if goal1[1] > goal2[0]:
    point1_12 = 3
    point2_12 = 0
elif goal1[1] == goal2[0]:
    point1_12 = 1
    point2_12 = 1
else:
    point1_12 = 0
    point2_12 = 3
#13
if goal1[2] > goal3[0]:
    point1_13 = 3
    point3_13 = 0
elif goal1[2] == goal3[0]:
    point1_13 = 1
    point3_13 = 1
else:
    point1_13 = 0
    point3_13 = 3
#14
if goal1[3] > goal4[0]:
    point1_14 = 3
    point4_14 = 0
elif goal1[3] == goal4[0]:
    point1_14 = 1
    point4_14 = 1
else:
    point1_14 = 0
    point4_14 = 3
#23
if goal2[2] > goal3[1]:
    point2_23 = 3
    point3_23 = 0
elif goal2[2] == goal3[1]:
    point2_23 = 1
    point3_23 = 1
else:
    point2_23 = 0
    point3_23 = 3
#24
if goal2[3] > goal4[1]:
    point2_24 = 3
    point4_24 = 0
elif goal2[3] == goal4[1]:
    point2_24 = 1
    point4_24 = 1
else:
    point2_24 = 0
    point4_24 = 3
#34
if goal3[3] > goal4[2]:
    point3_34 = 3
    point4_34 = 0
elif goal3[3] == goal4[2]:
    point3_34 = 1
    point4_34 = 1
else:
    point3_34 = 0
    point4_34 = 3
#result point
def pointall(x,y,z):
    all = x+y+z
    return all
point1all = pointall(point1_14 ,point1_12, point1_13) 
point2all = pointall(point2_12, point2_23, point2_24)
point3all = pointall(point3_13, point3_34, point3_23)
point4all = pointall(point4_14, point4_24, point4_34)
result = [point1all,point2all,point3all,point4all]
if result[0] == result[1]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum2-goal1[1]-goal3[1]-goal4[1]):
        result[0] += 0.01
        point1all += 0.01
        pass
    elif (sum1-goal2[0],goal3[0],goal4[0]) < (sum2-goal1[1]-goal3[1]-goal4[1]):
        result[1] += 0.01
        point2all += 0.01
    else:
        if sum1 > sum2:
            result[0] += 0.01
            point1all += 0.01
        else:
            result[1] += 0.01
        point2all += 0.01
elif result[0] == result[2]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[0] += 0.01
        point1all += 0.01
        pass
    elif (sum1-goal2[0],goal3[0],goal4[0]) < (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[2] += 0.01
        point3all += 0.01
    else:
        if sum1 > sum3:
            result[0] += 0.01
            point1all += 0.01
        else:
            result[2] += 0.01
            point3all += 0.01
elif result[0] == result[3]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[0] += 0.01
        point1all += 0.01
        pass
    elif (sum1-goal2[0],goal3[0],goal4[0]) < (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[3] += 0.01
        point4all += 0.01
    else:
        if sum1 > sum4:
            result[0] += 0.01
            point1all += 0.01
        else:
            result[3] += 0.01
            point4all += 0.01
elif result[1] == result[2]:
    if (sum2-goal1[1]-goal3[1]-goal4[1]) > (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[1] += 0.01
        point2all += 0.01
        pass
    elif (sum2-goal1[1]-goal3[1]-goal4[1]) < (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[2] += 0.01
        point3all += 0.01
    else:
        if sum2 > sum3:
            result[1] += 0.01
            point2all += 0.01
        else:
            result[2] += 0.01
            point3all += 0.01
elif result[1] == result[3]:
    if (sum2-goal1[1]-goal3[1]-goal4[1]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[1] += 0.01
        point2all += 0.01
        pass
    elif (sum2-goal1[1]-goal3[1]-goal4[1]) < (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[3] += 0.01
        point4all += 0.01
    else:
        if sum2 > sum4:
            result[1] += 0.01
            point2all += 0.01
        else:
            result[3] += 0.01
            point4all += 0.01
elif result[2] == result[3]:
    if (sum3-goal1[2]-goal2[2]-goal4[2]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[2] += 0.01
        point3all += 0.01
        pass
    elif (sum3-goal1[2]-goal2[2]-goal4[2]) < (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[3] += 0.01
        point4all += 0.01
    else:
        if sum3 > sum4:
            result[2] += 0.01
            point3all += 0.01
        else:
            result[3] += 0.01
            point4all += 0.01
result.sort()
result.reverse()
""""
if result[0] == result[1]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum2-goal1[1]-goal3[1]-goal4[1]):
        result[0] += 0.01
        pass
    else:
        result[1] += 0.01
elif result[0] == result[2]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[0] += 0.01
        pass
    else:
        result[2] += 0.01
elif result[0] == result[3]:
    if (sum1-goal2[0],goal3[0],goal4[0]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[0] += 0.01
        pass
    else:
        result[3] += 0.01
elif result[1] == result[2]:
    if (sum2-goal1[1]-goal3[1]-goal4[1]) > (sum3-goal1[2]-goal2[2]-goal4[2]):
        result[1] += 0.01
        pass
    else:
        result[2] += 0.01
elif result[1] == result[3]:
    if (sum2-goal1[1]-goal3[1]-goal4[1]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[1] += 0.01
        pass
    else:
        result[3] += 0.01
elif result[2] == result[3]:
    if (sum3-goal1[2]-goal2[2]-goal4[2]) > (sum4-goal1[3]-goal2[3]-goal3[3]):
        result[2] += 0.01
        pass
    else:
        result[3] += 0.01
result.sort()
result.reverse()
""" 
"""
    (sum1-goal2[0],goal3[0],goal4[0])
    (sum2-goal1[1]-goal3[1]-goal4[1])
    (sum3-goal1[2]-goal2[2]-goal4[2])
    (sum4-goal1[3]-goal2[3]-goal3[3])
"""
"""
#name
if result[0] == point1all:
    number1 = team1
if result[1] == point1all:
    number2 = team1
if result[2] == point1all:
    number3 = team1
if result[3] == point1all:
    number4 = team1    
if result[0] == point2all:
    number1 = team2
if result[1] == point2all:
    number2 = team2
if result[2] == point2all:
    number3 = team2
if result[3] == point2all:
    number4 = team2 
if result[0] == point3all:
    number1 = team3
if result[1] == point3all:
    number2 = team3
if result[2] == point3all: 
    number3 = team3
if result[3] == point3all:
    number4 = team3 
if result[0] == point4all:
    number1 = team4
if result[1] == point4all:
    number2 = team4
if result[2] == point4all:
    number3 = team4
if result[3] == point4all:
    number4 = team4          
"""
if max(result) == point1all:
    number1 = team1
elif max(result) == point2all:
    number1 = team2
elif max(result) == point3all:
    number1 = team3
elif max(result) == point4all:
    number1 = team4
del result[0]
if max(result) == point1all:
    number2 = team1
elif max(result) == point2all:
    number2 = team2
elif max(result) == point3all:
    number2 = team3
elif max(result) == point4all:
    number2 = team4
del result[0]
if max(result) == point1all:
    number3 = team1
elif max(result) == point2all:
    number3 = team2
elif max(result) == point3all:
    number3 = team3
elif max(result) == point4all:
    number3 = team4
del result[0]
if max(result) == point1all:
    number4 = team1
elif max(result) == point2all:
    number4 = team2
elif max(result) == point3all:
    number4 = team3
elif max(result) == point4all:
    number4 = team4
result = [point1all,point2all,point3all,point4all]
result.sort()
result.reverse()
#last print
print(f'{number1} {int(result[0])}')
print(f'{number2} {int(result[1])}')
print(f'{number3} {int(result[2])}')
print(f'{number4} {int(result[3])}')
"""
#table
print(*goal1)
print(*goal2)
print(*goal3)
print(*goal4)
"""