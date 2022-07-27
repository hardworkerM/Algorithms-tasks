import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    left = []
    equal = []
    right = []
    element = random.choice(arr)
    for i in arr:
        if i > element:
            right.append(i)
        elif i < element:
            left.append(i)
        else:
            equal.append(i)
    left = quick_sort(left)
    right = quick_sort(right)
    out = left + equal + right
    return out


def output(finish):
    d = list(finish.keys())
    d = quick_sort(d)
    for i in d:
        print(i, finish[i][1])


data = input().split()
n = int(data[0])
report_type = data[1]


days_data = {}


if report_type == 'daily':
    for i in range(n):
        data = input().split()
        day = int(data[0])
        id = data[1]
        if day in days_data:
            if id not in days_data[day][0]:
                days_data[day][0][id] = 1
                days_data[day][1] += 1
        else:
            days_data[day] = [{id: 1}, 1]
    output(days_data)


elif report_type == 'weekly':
    for i in range(n):
        data = input().split()
        day = int(data[0])
        month = day // 7
        id = data[1]
        if month in days_data:
            if id not in days_data[month][0]:
                days_data[month][0][id] = 1
                days_data[month][1] += 1
        else:
            days_data[month] = [{id: 1}, 1]
    output(days_data)


elif report_type == 'quarterly':
    for i in range(n):
        data = input().split()
        day = int(data[0])
        quarterly = day // 90
        id = data[1]
        if quarterly in days_data:
            if id not in days_data[quarterly][0]:
                days_data[quarterly][0][id] = 1
                days_data[quarterly][1] += 1
        else:
            days_data[quarterly] = [{id: 1}, 1]
    output(days_data)



