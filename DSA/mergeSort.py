def merge_sort(arr):

    if len(arr) > 1:

        left = arr[:len(arr)//2]   # slicing the array from start to half
        right = arr[len(arr)//2:]  # slicing the array from half to end

        #recursion
        merge_sort(left)
        merge_sort(right)

        # now merging

        i = j = k = 0    # i to keep track of left array, j for right and k to keep track of the merged array

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j +=1

            k += 1

        while i < len(left):

            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            arr[k] = right[j]
            j += 1
            k += 1

array = [3,4,7,-1,2,5,6,1,7,7]
print("Before merge soritng : ", array)
merge_sort(array)
print("after merge sorting : ", array)

