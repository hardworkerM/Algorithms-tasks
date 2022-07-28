def date_in_numb(date, start_year):
    numb = 0
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    years = sum([made_y_in_d(i) for i in range(start_year, year)])
    month = sum([made_m_in_d(i, year) for i in range(0, month)])
    numb = day + month + years
    return numb


def made_m_in_d(m, y):
    if m < 1:
        return 0
    elif m in [1, 2, 3, 4, 5, 6, 7]:
        if m % 2 == 1:
            days = 31
        else:
            if m == 2:
                if y % 4 == 0:
                    days = 29
                else:
                    days = 28
            else:
                days = 30
    else:
        if m % 2 == 1:
            days = 30
        else:
            days = 31
    return days


def made_y_in_d(y):
    if y % 4 == 0:
        return 366
    return 365


def distance(timeline):
    dist = []
    for i in range(len(timeline) - 1):
        space = timeline[i + 1] - timeline[i] - 1
        dist.append(space)
    return max(dist)


def main(dates, l, k):
    timeline = []
    for date in dates:
        line = date_in_numb(date, l)
        timeline.append(line)
    k2 = str(int(k) + 1)
    line = date_in_numb(f'01-01-{k2}', l)
    timeline.append(line)
    timeline.append(0)
    timeline = sorted(timeline)
    dist = distance(timeline)
    return dist


# n, l, r = [int(i) for i in input().split()]
# dates = []
# for i in range(n):
#     dates.append(input())
# print(main(dates, l, r))


def test1():
    n = 10
    l = 2020
    k = 2020
    dates = [
        '10-01-2020',
        '01-01-2020',
        '29-02-2020',
        '01-03-2020',
        '01-04-2020',
        '01-05-2020',
        '01-06-2020',
        '01-07-2020',
        '01-08-2020',
        '01-09-2020',
        '01-12-2020'
    ]

    res = main(dates, l, k)
    answer = 90
    print(res, res == answer)


def test2():
    n = 11
    l = 2020
    k = 2020
    dates = [
        '01-01-2020',
        '02-02-2020',
        '03-03-2020',
        '04-04-2020',
        '10-10-2020',
        '11-11-2020',
        '05-05-2020',
        '06-06-2020',
        '07-07-2020',
        '08-08-2020',
        '09-09-2020'
    ]
    res = main(dates, l, k)
    answer = 50
    print(res, res == answer)



def test_my():
    n = 3
    l = 2020
    k = 2020
    dates = [
        '01-01-2020',
        '02-01-2020',
        '03-01-2020',

    ]
    main(dates, l, k)

    n = 3
    l = 2020
    k = 2020
    dates = [
        '01-01-2020',
        '01-01-2020',
        '01-01-2020',

    ]

test1()
test2()
