sentence = input('Enter sentence')


def count_sym(text):
    return {i: text.count(i) for i in text}


print(count_sym(sentence))


def try_p(*args):
    pass


def biggest(a, b):
    if a > b:
        return a
    else:
        return b


print(biggest(4, 5))


def sum_ints(*args):
    return sum(args)


print(sum_ints(1, 2, 3, 4))


def calc_(num1, num2, func):
    match func:
        case '+':
            return (num1 + num2)
        case '-':
            return (num1 - num2)
        case '*':
            return (num1 * num2)
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return('ERROR')

print(calc_(2, 3, '-'))

cache = []


def add_cache(item):

    if item in cache:
        return 'Item exists in the list'
    else:
        cache.append(item)
    return cache

print(add_cache('Text'))
print(add_cache('Hello'))


week = {7: 'Sun', 4: 'Mon', 5: 'Tues', 6: 'Thur', 4: 'Fri', 5: 'Sat', 6: 'Wed'}
sorted_list =[]
for i in week.keys():
    sorted_list.append(i)
sorted_list.sort()

print(sorted_list)


def inter_set(list1, list2):
    intersection_set = set(list1).intersection(set(list2))
    return intersection_set


print(inter_set([1, 2, 3, 4], [3, 4, 5, 6]))






def uniq_test(list1):
    return len(set(list1)) == len(list1)

print(uniq_test([1, 3, 4, 5, 2, 3, 4]))



def turn_to_set(entry_list):
    return list(set(entry_list))


print(turn_to_set([1, 2, 3, 4, 5, 6, 5, 6, 7]))


