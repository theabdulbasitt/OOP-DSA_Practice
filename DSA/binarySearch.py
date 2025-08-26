def binarySearch (arr, num):
    low = 0
    high  = len(arr) - 1

    while low <= high:

        mid  = low + (high - low) // 2

        if arr[mid] == num:
            return mid
        
        elif arr[mid] < num:
            low = mid + 1

        else:
            high = mid - 1


    return -1


numbers = [1,2,3,4,5,6,7,8,9,12,15,24,54]

results = binarySearch(numbers, 1)

if results >= 0:
    print("The element is present at index : ",results)

else:
    print("Elment does not exists")

