
n = int(input())
m = []
for i in range(n):
    inp = input().split()
    if inp[0] == "insert":
        m.insert(int(inp[2]),int(inp[1]))
    elif inp[0] == "remove":
        m.remove(int(inp[1]))
    elif inp[0] == "append":
        m.append(inp[1])
    elif inp[0] == "sort":
        m.sort()
    elif inp[0] == "pop":
        m.append(inp[1])
    elif inp[0] == "reverse":
        m.reverse()
    elif inp[0] == "print":
        print(m)













# for i in range(n):
#     if i < n/2:
#         m.append(int(i+n/5))
#     print(m)
#     if  i > n/2 :
#         m.pop()
#     if i == int(n/2 +1):
#         m.insert(0,10)
#     # m.sort()
#     # m.reverse()
#     # # m.remove(10)
#     # print(m)











    # if i <= N/3:
    #     print(i)
    # #     m.append(i+5)
    # # print(m)
    # if ((i > N/3)and (i <= N )):
    #     print(i+1)