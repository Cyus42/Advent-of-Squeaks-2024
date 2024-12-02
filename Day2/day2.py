# vars we need
data = []
safe_count = 0
somewhat_safe_count = 0
#Initailize the file, format them as lists
with open('d2data.txt','r') as file:
    for line in file:
        data.append(list(map(int,line.split())))
#This is, surprisingly, mostly math. 
for row in data:
    if all(
        row[i] < row[i + 1] and (row[i + 1] - row[i] <= 3)
        for i in range(len(row)-1)
    ) or all(
        row[i] > row[i + 1] and (row[i] - row[i + 1] <= 3)
        for i in range(len(row)-1)
    ):  safe_count += 1
#Part 2, This is rewritten after trying the hard way. Lets do the easy way. Removing numbers one at a time. 
#Lets make this a function. 
def is_valid(row):
    return all(
        row[i] < row[i + 1] and (row[i + 1] - row[i] <= 3)
        for i in range(len(row)-1)
    ) or all(
        row[i] > row[i + 1] and (row[i] - row[i + 1] <= 3)
        for i in range(len(row)-1)
    )
#Now we process every line, muahaha
for row in data:
    valid_copy = False
    for i in range(len(row)):
        row_copy = row[:i] + row[i+1:] #this creates a new row from everything before and after i
        if is_valid(row_copy):
            valid_copy = True
            break
    if valid_copy:
        somewhat_safe_count += 1

#Solution for part 1
print("Absolutely Safe:", safe_count)
#Solution for part 2
print("Somewhat Safe:", somewhat_safe_count)

# yeah, i had AI write this code. im not doing well -w-
