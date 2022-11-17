import DEPQ
import os

buffer = []
global_var = 0
gjob = []

# Merging File
def mergingFile(file1,file2,file3):
    global global_var
    global_var = global_var - 1
    # print(f"Merging file {file1}, {file2} and {file3}")

    bjob = open(file2, "r")
    bjobData = bjob.readlines()
    bjob.close()

    ajob = open(file1, "a")
    ajob.write(" ")
    for _ in bjobData:
        ajob.write(_)
    ajob.close()

    djob = open(file1, "r")
    djobData = djob.readlines()
    djob.close()

    gjob = open(file3, "r")
    gjobData = gjob.readlines()
    gjob.close()

    fjob = open(file2, "w")
    for __ in djobData:
        fjob.write(__)
    fjob.write(" ")
    for i in gjobData:
        fjob.write(i)
    fjob.close()
    os.remove(f"E:/DOR/Code/ExternalSorting/ExternalSorting/{file3}")
    os.remove(f"E:/DOR/Code/ExternalSorting/ExternalSorting/{file1}")

    return file2


# Main funtion of external sorting
def externalDataSorting(filename,Depq):
    file = open(filename, "r")
    ajob = file.readlines()
    file.close()
    # print(ajob)
    wjob = []
    bjob = []
    minDataList = []
    maxDataList = []

    for _ in ajob:
        cjob = [i for i in _.split(" ")]
        wjob = wjob+cjob
    wjob.pop()

    for i in range(len(wjob)):
        bjob.append(int(wjob.pop(0)))

    # print(bjob)
    num = len(bjob)
    if num <= 30:
        # print(f"Inside the small sorting!")
        while len(bjob):
            a = bjob.pop(0)
            Depq.insertintoDEPQ(a)

        for l in range(num - 1):
            Depq.deleteminimumElementDEPQ()
        gjob.append(Depq.buffer.pop(0))
        Depq.minq.display()

        Depq.maxq.display()
        print(gjob)
        sjob = open(filename, "w")
        while len(gjob):
            sjob.write(f"{gjob.pop(0)} ")
        sjob.close()
        return filename

    global global_var
    global_var = global_var + 1

    mjob = []
    for i in range(30):
        mjob.append(bjob.pop(0))

    while len(mjob):
        a = mjob.pop(0)
        Depq.insertintoDEPQ(a)
    num = len(bjob)

    while(len(bjob)):
        a = bjob.pop(0)
        if a < Depq.minq.root.data:
            minDataList.append(a)
        elif a > Depq.maxq.root.data:
            maxDataList.append(a)
        else:
            minDataList.append(Depq.minq.root.data)
            Depq.deleteminimumElementDEPQ()
            Depq.insertintoDEPQ(a)


    while len(gjob):
        gjob.pop(0)


    for l in range(30):
        Depq.deleteminimumElementDEPQ()
    gjob.append(Depq.buffer.pop(0))


    number_of_element_small_list = len(minDataList)
    number_of_element_large_list = len(minDataList)



    sjob = open(filename, "w")
    while len(gjob):
        sjob.write(f"{gjob.pop(0)} ")
    sjob.close()

    jjob = open(f"newFileSmallerData{global_var}.txt","w")
    while len(minDataList):
        jjob.write(f"{minDataList.pop(0)} ")
    jjob.close()

    ljob = open(f"newFileLargerData{global_var}.txt","w")
    while len(maxDataList):
        ljob.write(f"{maxDataList.pop(0)} ")
    ljob.close()

    if number_of_element_small_list != 0:
        # print("function is called for small data!")
        filename = externalDataSorting(f"newFileSmallerData{global_var}.txt",Depq)


    if number_of_element_large_list != 0:
        # print("function is called for Large data!")
        filename = externalDataSorting(f"newFileLargerData{global_var}.txt",Depq)
    zjob = mergingFile(f"newFileSmallerData{global_var}.txt",filename,f"newFileLargerData{global_var}.txt")

    return zjob


if __name__ == "__main__":
    Depq = DEPQ.DoubleEndedQueue()

    fileData = externalDataSorting("data.txt",Depq)
    # print(f"fileData value : {fileData}")

    displayData = open(fileData,"r")
    wjob = displayData.readlines()
    displayData.close()
    print(wjob)
