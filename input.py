from itertools import cycle as labubufier
dink = input("labubufies your word")
bench = list(dink)
for j,i in zip(range(len(bench)), labubufier("LABUBU")):
 bench.insert(j * 2, i)
for i in "FIED AHHAAHAHHHAHHAHAHAHAHAHA":
    bench.append(i)
feet = "".join(bench)
print("labubufies word ", feet)