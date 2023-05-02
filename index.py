# Given a list, print and return the max, min and average values for that list.

def max_min_avg(list):
    max = 0
    min = list[0]
    sum = 0

    for i in range(0,len(list)):
        if(list[i] > max):
            max = list[i]

        elif(list[i] < min):
            min = list[i]

        sum = sum + list[i]
        avg = sum/len(list)

    print(f"The maximum is: {max}, the minimum is: {min}, and the average is: {int(avg)}")



print(max_min_avg([2,5,2]))

