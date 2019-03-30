#Implementing Insertion Sort
class Sort:
 def insertion_sort(self):

    total_num = 0
    data = []

    total_num = (int(input("Enter total numbers you want to sort=")))
    for i in range(total_num):
        data.append(int(input("Enter num")))

    for i in range(data.__len__()):
        j = i
        temp = data[i]
        while (j > 0 and data[j - 1] > temp):
            data[j] = data[j - 1]
            j -= 1
        data[j] = temp

    print("Printitng sorted list")
    for i in range(data.__len__()):
        print(data[i])

