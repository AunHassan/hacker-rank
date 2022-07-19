record = []
marks = []
for i in range(int(input("no of students:"))):
        name = input("name:")
        score = float(input("marks:"))
        record += [[name,score]]
        marks += [score]
sl = (sorted(set(marks)))[1]
print(sl)
for i,j in sorted(record):
    if j == sl:
        print(i)

