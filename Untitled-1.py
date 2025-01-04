# Bemenet: n es t lista
n = 8
t = [6400, -2000, -4300, 8200, 1000, -3400, 600, -900]

# C Feladat: Többször nyertünk vagy veszítettünk?
n = 8
t = [6400, -2000, -4300, 8200, 1000, -3400, 600, -900]

nyereseg_szam = sum(1 for i in t if i > 0)
veszteseg_szam = sum(1 for i in t if i < 0)

if nyereseg_szam > veszteseg_szam:
    print("Többször nyertünk, mint veszítettünk.")
elif nyereseg_szam < veszteseg_szam:
    print("Többször veszítettünk, mint nyertünk.")
else:
    print("Ugyanannyiszor nyertünk, mint veszítettünk.")

print("d) feladat --------------------")
maxindex=0
maxhossz=0
index=0
hossz=0
for i in range(1,n):
    if t[i]>0:
        hossz +=1
        if hossz == 1:
            index = i+1
    elif t[i]<0:
        if maxhossz < hossz:
            maxindex = index
            maxhossz = hossz
        hossz = 0
        index = 0
if maxhossz > 0:
    print("A",maxindex,". és",maxindex+maxhossz-1,". hét között volt",maxhossz,"héten keresztül a leghosszabb nyerő sorozat.")
else:
    print("Nincs nyerő sorozat.")
