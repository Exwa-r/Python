num = int(input())
# c = 1

# for i in range(0,num):
#     pattern = ""
#     for j in range(0,i+1):
#         pattern += str(c) + " "
#         c += 1
#     print(pattern)


# for i in range(0,num):
#     pattern = ""
#     for j in range(0,num):
#         if i == 0 or i == num-1 or j == 0 or j == num-1:
#             pattern += "*"
#         else:
#             pattern += " "
#     print(pattern)

for i in range(0,num*2-1):
    pattern = ""
    for j in range(0,num*2-1):
        if i < num:
            for k in range (1,num-i):
                pattern += " "
        elif i == num:
            continue
        elif i > num:
            for k in range(i):
                pattern += " "
        if i < 5 or i > 5:
            pattern += " "



















    for k in range(0,num*2-1):
        if i <= 5:
            pattern += "*"
    print(pattern)