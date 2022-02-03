
numbers_string = input("enter the numbers:")
count1 = count2 = 0
numbers_list = numbers_string.split(",")
for i in range(0, len(numbers_list), 1):
    numbers_list[i] = int(numbers_list[i])
    if(numbers_list[i] > 0):
        count1 += 1
    else:
        count2 += 1

print("numbers_list=", numbers_list)
print("positive numbers in list:", count1)
print("negative numbers in list:", count2)
