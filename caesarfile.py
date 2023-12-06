import sys
a = []
with open(sys.argv[1], "r") as f:
    for chara in f:
        for bling in chara:
            a.append(ord(bling))
c = int(sys.argv[2])
b = lambda b: print(chr(b-c), end="")
(list(map(b, a)))
print("")