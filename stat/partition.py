def partition(ar, old_ar, maxlen):
    for idx, elm in enumerate(ar):
        if maxlen < 2:
            outcomes.append( " ".join(old_ar+[elm]) )
        else:
            new_ar = ar[:idx]+ar[idx+1:]
            new_old_ar = old_ar+[elm]
            partition(new_ar,new_old_ar, maxlen-1)

ar = raw_input().split()
outcomes = []
partition(ar, [], len(ar))
for elm in set(outcomes):
    print elm
