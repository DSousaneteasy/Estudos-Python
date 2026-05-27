import collections


MyList = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]

ListCount = collections.Counter(MyList)


print(ListCount)


for Item in ListCount:
    print("Item: ", Item, " Appears: ", ListCount[Item])


print("The value 1 appears 4 times.")
