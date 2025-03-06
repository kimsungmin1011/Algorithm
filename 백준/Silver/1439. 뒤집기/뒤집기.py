s = list(input())

count0 = 0
count1 = 0
flag1 = False
flag0 = False

for i in s:
    if int(i) == 1:
        if flag0 == True:
            flag0 = False

        if flag1 == False:
            flag1 = True
            count1 += 1
        else:
            continue
    else:
        if flag1 == True:
            flag1 = False

        if flag0 == False:
            flag0 = True
            count0 += 1
        else:
            continue

print(min(count0, count1))
