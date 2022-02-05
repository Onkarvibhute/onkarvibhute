numbers_list = list()
k=0
for i in range(0, 2, 1):
    choice = input("Do you want to add number:")
    if(choice == "y"):
        number = int(input("number="))
        if number not in numbers_list:
            if number > 0:
                numbers_list.append(number)
            if number < 0:
                i-=1
                print("no to add negative number:")
        else:
            print("number is already present in the list")
    else:
        break
print("numbers_list:", numbers_list)
