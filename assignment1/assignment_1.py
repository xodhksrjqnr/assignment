## 함수 부분 ##
def conversion(array, number_array):
    error = 0
    for data in array[3:]:
        try:
            tmp = int(data)
        except ValueError:
            print("Error! 정수가 아닌 값이 있습니다.")
            error = 1
            break
        else:
            number_array.append(tmp)
    return error

def quicksort_a(arr1, left, right):
    pivot = arr1[left]
    low = left
    high = right
    while low < high:
        while arr1[high] >= pivot and low < high:
                high -= 1
        if left < right:
                arr1[low] = arr1[high]
        while arr1[low] <= pivot and low < high:
                low += 1
        if not low < high:
                break
        arr1[high] = arr1[low]
        high -= 1
    arr1[low] = pivot
    if low > left:
            quicksort_a(arr1, left, low-1)
    if low < right:
            quicksort_a(arr1, low+1, right)
    
def quicksort_d(arr1, left, right):
    pivot = arr1[left]
    low = left
    high = right
    while low < high:
        while arr1[high] <= pivot and low < high:
                high -= 1
        if left < right:
                arr1[low] = arr1[high]
        while arr1[low] >= pivot and low < high:
                low += 1
        if not low < high:
                break
        arr1[high] = arr1[low]
        high -= 1
    arr1[low] = pivot
    if low > left:
            quicksort_d(arr1, left, low-1)
    if low < right:
            quicksort_d(arr1, low+1, right)

## 메인 코드 부분 ##
arr = input()
array = []
number_array = []
array = arr.split()

if array[0] == '-o' and array[2] == '-i':
    if array[1] == 'A':
        e = conversion(array, number_array)
        if e == 0:
            size = len(number_array)
            quicksort_a(number_array, 0, size-1)
            print(number_array)
    elif array[1] == 'D':
        e = conversion(array, number_array)
        if e == 0:
            size = len(number_array)
            quicksort_d(number_array, 0, size-1)
            print(number_array)
    else :
        print("잘못된 입력입니다.")
else :
    print("잘못된 입력입니다.")