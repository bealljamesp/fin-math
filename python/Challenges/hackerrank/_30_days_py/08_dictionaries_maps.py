n = int(input())
d = {}

for i in range(n):
    x = input().split()
    d[x[0]] = x[1]

while True:
    try:
        NAME = input()
        if NAME in d:
            print(NAME, "=", d[NAME], sep="")
        else: print("Not found")
    except:
        break

    3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
    
# sam=99912222
# Not found
# harry=12299933