import os

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def external_sort(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
        data = [int(i) for i in data]
        sorted_data = merge_sort(data)
        
        with open("sorted_" + file_name, "w") as sorted_file:
            for i in sorted_data:
                sorted_file.write(str(i) + "\n")

file_name = input("Enter the file name: ")
external_sort(file_name)
print("File sorted successfully")
