length,width = input().split()
length = int(length)
width  = int(width)

c = ".|."
#-----------top cone-------------
for i in range(1,length,2):
    print((c*i).center(width,"-"))
#-----------welcome-------------
print("WELCOME".center(width,"-"))
#-----------bottom cone-------------
for i in reversed(range(1,length,2)):
    print((c*i).center(width,"-"))