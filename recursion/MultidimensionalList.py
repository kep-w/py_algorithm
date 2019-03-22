
lst = [[2,3],[1,5],[4,6]]
temp = []


def func(lst):
    for i in lst:
        if not isinstance(i, list):
            temp.append(i)
        else:
            func(i)


func(lst)
print(temp)