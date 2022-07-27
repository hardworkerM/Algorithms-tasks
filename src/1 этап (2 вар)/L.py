def count_s_len(diff_alnum):
    s_min_length = (diff_alnum // 2) + 1
    return s_min_length


def check_pare(pare, s_len):
    diffs = []
    count = 0
    for i in pare:
        if i[1] not in diffs:
            diffs.append(i[1])
            count += 1
    if count < s_len:
        return 0
    return 1


def make_s_len(arr_to_check):
    arr_to_check = arr_to_check[1:-1]
    count = 0
    for digit in arr_to_check:
        count += int(digit[0])
    return count + 2


def count_alnum(a):
    count = []
    diff_alnum = 0
    len_a2 = 0
    line2 = []
    number = ''
    for i in a:
        if i.isdigit():
            number += i
        else:
            if i not in count:
                count.append(i)
                diff_alnum += 1
            if not number:
                number = '1'
            line2.append([number, i])
            len_a2 += 1
            number = ''
    return line2, diff_alnum, len_a2


def main(line):
    line2, count_alpha, line2_length = count_alnum(line)
    s_min_length = count_s_len(count_alpha)
    if s_min_length == 1:
        return 1
    if s_min_length == 2:
        return 2
    min_s = 0
    i = 0
    while i - 1 != line2_length - s_min_length:
        j = s_min_length
        pare = line2[i: i + j]
        flag = check_pare(pare, s_min_length)
        while not flag and i + j < line2_length:
            j += 1
            pare = line2[i: i + j]
            flag = check_pare(pare, s_min_length)
            if pare[-1] == pare[0]:
                i += 1
                j = s_min_length
        if flag:
            s_len2 = make_s_len(pare)
            if min_s == 0:
                min_s = s_len2
            elif min_s > s_len2:
                min_s = s_len2
        i += 1
    return min_s


def test():
    t1 = 'A5B5CDEF5X5YZ', 5
    t2 = '9W3B24WB14W', 2
    t3 = 'D9W3B24M25K24LWB14WC', 14
    t4 = '1000000000A', 1

    test1 = [t1, t2, t3, t4]

    for t in test1:
        answer = main(t[0])
        check = t[1]
        print(answer, answer == check)

test()
