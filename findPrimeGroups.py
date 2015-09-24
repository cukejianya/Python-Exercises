def findPrimeGroups(p_array, diff_array):
    prime_groups = []
    for elm in p_array:
        for idx, diff in enumerate(diff_array):
            if not elm+diff in p_array:
                break
            if idx == len(diff_array)-1:
                prime_groups.append([elm]+[elm+x for x in diff_array])


    return prime_groups
p = [int(x) for x in raw_input().split()]
d = [int(x) for x in raw_input().split()]
for ar in findPrimeGroups(p, d):
    print ar
