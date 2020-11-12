def jaccard(set1, set2):
    a = 0
    for i in set1:
        if i in set2:
            a += 1
    b = a / (len(set1) + len(set2) - a)
    return b

set1 = {1,2,3,4,5}
set2 = {3,8,5,6,7}

print(jaccard(set1, set2))
