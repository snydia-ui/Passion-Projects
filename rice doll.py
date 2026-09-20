import random
input("all possible combinations of 6 rolled dice(will not show dupes uwu):")
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                for m in range(1,7):
                    for n in range(1,7):
                        prinetetet = [i,j,k,m,n]
                        random.shuffle(prinetetet)
                        pri = str(prinetetet)
                        pri =pri.replace("]", "")
                        pri =pri.replace(",", " ")
                        pri = pri.replace("[", "")
                        print(pri)
input("same thing but printed diff")
from itertools import product
all_combos = list(product(range(1, 7), repeat=6))
random.shuffle(all_combos)

for combo in all_combos:

    print(*(combo))