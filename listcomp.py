x = int(input("input x:"))
y = int(input("input y:"))
z = int(input("input z:"))
n = int(input("input n:"))
xa = [i for i in range (x+1)]
ya = [j for j in range (y+1)]
za = [k for k in range (z+1)]
print(xa)
print(ya)
list = [[x,y,z]for x in xa for y in ya for z in za]
print(list)
for i in list:
    if sum(i)!= n:
        print(i)