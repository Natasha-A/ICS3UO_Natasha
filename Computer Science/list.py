
list1 = ["1", "2", "3"]
list2 = ["a", "b"]

def combine(list1, list2):
    list3 = []

    for x in range(len(list2)):
        for y in range(len(list1)):
            list3.append(list1[y] + list2[x])

    return list3

listOne = combine(list1, list2)

print(listOne)

