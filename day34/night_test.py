#1

def insert(values):
    for i in range(1, len(values)):
        temp = values[i]
        pos = i
        for j in range(i-1, -1, -1):
            if values[j] > temp:
                values[j+1] = values[j]
                pos = j
            else:
                pos = j + 1
                break
        values[pos] = temp

values = [80, 90, 121, 34, 56, 90 , 73, 98, 12, 43]

insert(values)
print(values)





















































