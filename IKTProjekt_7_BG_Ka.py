#Bálint Gábor 10.B és Kaibás Alex 10.B - Python első beadandó
print("a) feladat --------------------")
n=8
t=[6400, -2000, -4300, 8200, 1000, -3400, 600, -900]
maxny=0
maxindex=0
nyossz=0
for i in range(n):
    nyossz+=t[i]
    if maxny < nyossz:
        maxny = nyossz
        maxindex = i+1
print(maxindex,". héten volt a legnagyobb a nyereségünk.")
