import DEPQ
import os

buffer = []
file_counter = 0
global_list = []

# Merging File
def mergePassFuntion(file1,file2,file3):
    global file_counter
    file_counter = file_counter - 1
    # print(f"Merging file {file1}, {file2} and {file3}")

    file_data=[]
    with open(file2, "r") as fp2:
        file_data = fp2.readlines()

    with open(file1, "a") as fp1:
        fp1.write(" ")
        for x in file_data:
            fp1.write(x)

    data_list=[]
    with open(file1, "r") as fp:
        data_list = fp.readlines()

    global_list=[]
    with open(file3, "r") as fp3:
        global_list = fp3.readlines()

    with open(file2, "w") as fp:
        for x in data_list:
            fp.write(x)
        fp.write(" ")
        for item in global_list:
            fp.write(item)
    # "C:\Users\haris\Downloads\ExternalSorting-main\ExternalSorting-main\ExternalSorting\large_data1.txt"
    # os.remove(f"C:/Users/haris/Downloads/ExternalSorting-main/ExternalSorting-main/ExternalSorting/{file3}")
    # os.remove(f"C:/Users/haris/Downloads/ExternalSorting-main/ExternalSorting-main/ExternalSorting/{file1}")

    return file2


# Main funtion of external sorting
def externalSort(filename,Depq):
    with open(filename, "r") as file:
        element_list = file.readlines()
    # print(element_list)
    data_list = []
    minDataList = []
    maxDataList = []

    for item in element_list:
        item = item.strip()
        # print(item)
        data = [int(i) for i in item.split(" ") if i!='']
        # print(data)
        data_list = data_list+ data
    # print(data_list)
    # print(data_list)
    num = len(data_list)
    if num <= 10:
        # print(f"Inside the small sorting!")
        while len(data_list):
            a = data_list.pop(0)
            Depq.insertintoDEPQ(a)
        # print(Depq.minq.root.val)
        # Depq.minq.display()
        # Depq.maxq.display()
        # Depq.minq.displayCorrespondance()
        # Depq.maxq.displayCorrespondance()

        for l in range(num-1):
            deleted_data=Depq.deleteminimumElementDEPQ()
            global_list.append(deleted_data)
        # print(global_list,"hooooooooo")
        
        # global_list.append(Depq.buffer[0])
        # print(global_list)
        with open(filename, "w") as fp:
            while len(global_list):
                fp.write(f"{global_list.pop(0)} ")
        return filename

    global file_counter
    file_counter = file_counter + 1

    data = []
    for i in range(10):
        data.append(data_list.pop(0))
    # print(data)
    while len(data):
        a = data.pop(0)
        Depq.insertintoDEPQ(a)
    num = len(data_list)
    # print(data_list)
    # print(num)
    # Depq.minq.display()
    # Depq.maxq.display()
    # Depq.minq.displayCorrespondance()
    # Depq.maxq.displayCorrespondance()
    # print(Depq.minq.root.val)
    while(len(data_list)):
        a = data_list.pop(0)
        # print(a,"-----",Depq.minq.root.val,Depq.maxq.root.val)
        if a < Depq.minq.root.val:
            minDataList.append(a)
        elif a > Depq.maxq.root.val:
            maxDataList.append(a)
        else:
            minDataList.append(Depq.minq.root.val)
            d = Depq.deleteminimumElementDEPQ()
            Depq.insertintoDEPQ(a)
        # print(Depq.minq.root.val,"----mini-----")

    # Depq.minq.display()
    # Depq.maxq.display()
    # print(Depq.minq.root.val)
    # print("max",maxDataList)
    # print("min",minDataList)

    while len(global_list):
        global_list.pop(0)

    # Depq.minq.displayCorrespondance()
    for l in range(10-1):
        deleted_data=Depq.deleteminimumElementDEPQ()
        # print(deleted_data,Depq.buffer)
        global_list.append(deleted_data)
    global_list.append(Depq.buffer[0])
    small_element_len = len(minDataList)
    larger_element_len = len(maxDataList)

    print(small_element_len,larger_element_len)
    print(global_list)
    print(minDataList)
    print(maxDataList)

    with open(filename, "w") as fp:
        while len(global_list):
            fp.write(f"{global_list.pop(0)} ")

    with open(f"small_data{file_counter}.txt","w") as fp1:
        while len(minDataList):
            fp1.write(f"{minDataList.pop(0)} ")

    with open(f"large_data{file_counter}.txt","w") as fp2:
        while len(maxDataList):
            fp2.write(f"{maxDataList.pop(0)} ")
    if small_element_len != 0:
        # print("function is called for small data!")
        filename = externalSort(f"small_data{file_counter}.txt",Depq)


    if larger_element_len != 0:
        # print("function is called for Large data!")
        filename = externalSort(f"large_data{file_counter}.txt",Depq)
    merged_file = mergePassFuntion(f"small_data{file_counter}.txt",filename,f"large_data{file_counter}.txt")

    return merged_file


if __name__ == "__main__":
    Depq = DEPQ.DoubleEndedQueue()

    fileData = externalSort("data.txt",Depq)
    # print(f"fileData value : {fileData}")

    file_list=[]
    with open(fileData,"r") as fp:
        file_list = fp.readlines()
    
    print(file_list)
