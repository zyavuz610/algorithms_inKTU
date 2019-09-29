#Enhanced quick sort
array=[54,26,93,17,77,31,44,55,20]
def quick_sort(left , right):
    right1 = right
    left1 = left
    if array[right1]> array[left1]:

        if array[(left1+right1) // 2] > array[right1]:
            pivot=array[right1]
        else:
            if array[(left1+right1) // 2]>array[left1]:
                pivot=array[(left1+right1) // 2]
            else:
                pivot=array[left1]

    else:
        if array[(left1+right1) // 2]>array[left1]:
            pivot=array[left1]
        else:
            if array[(left1+right1) // 2]>array[right1]:
                pivot=array[(left1+right1) // 2]
            else:
                pivot=array[right1]
    while right1>= left1:

        while (pivot<array[right1]):
            right1=right1-1
        while (pivot>array[left1]):
            left1=left1+1
        if left1<=right1 :
            if right1 != left1 :
                temp = array[left1]
                array[left1] = array[right1]
                array[right1] = temp
            right1 =right1-1
            left1=left1+1

    if left <right1:
        quick_sort(left , right1)
    if right > left1:
        quick_sort(left1, right)


quick_sort(0,len(array)-1)
print("sıralanmış dizi:" , array )