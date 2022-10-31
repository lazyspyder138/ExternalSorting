## Double Ended Priority Queue Implementation Using Python!
import random
import os

# Create Node 
class priorityQueueNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
        self.back = None
        self.mapData = None

# Class for implementing DEPQ
class queueImplementation:
    def __init__(self):
        self.root = None
        self.insertPointNode = None
        self.lastNode = None

    # Adjust MinHeap during insertion

    def adjustMinHeap(self, node):
        if node == None or node.parent == None:
            return
        if node.data < node.parent.data:
            tell = node.data
            node.data = node.parent.data
            node.parent.data = tell


            temp = node.mapData
            node.mapData = node.parent.mapData
            node.parent.mapData = temp

            if node.parent:
                self.adjustMinHeap(node.parent)

    # Adjust MaxHeap during insertion

    def adjustMaxHeap(self, node):
        if node == None or node.parent == None:
            return
        if node.data > node.parent.data:
            tell = node.data
            node.data = node.parent.data
            node.parent.data = tell

            temp = node.mapData
            node.mapData = node.parent.mapData
            node.parent.mapData = temp

            if node.parent:
                self.adjustMaxHeap(node.parent)

    # Adjust MinHeap during deletion

    def adjustMin(self,node):
        if node==None or (node.left == None and node.right==None):
            return
        if node.left != None and node.right == None:
            if node.left.data < node.data:
                temp = node.data
                node.data = node.left.data
                node.left.data = temp

                tell = node.mapData
                node.mapData = node.left.mapData
                node.left.mapData = tell


        else:
            if node.left.data < node.right.data:
                if node.left.data < node.data:
                    temp = node.left.data
                    node.left.data = node.data
                    node.data = temp

                    tell = node.mapData
                    node.mapData = node.left.mapData
                    node.left.mapData = tell

                    if node.left:
                        self.adjustMin(node.left)
            else:
                if node.right.data < node.data:
                    temp = node.right.data
                    node.right.data = node.data
                    node.data = temp

                    tell = node.mapData
                    node.mapData = node.right.mapData
                    node.right.mapData = tell

                    if node.right:
                        self.adjustMin(node.right)

    # Adjust MaxHeap during deletion
    def adjustMax(self, node):
        if node==None or (node.left == None and node.right==None):
            return
        if node.left != None and node.right == None:
            if node.left.data > node.data:
                temp = node.left.data
                node.left.data = node.data
                node.data = temp

                tell = node.mapData
                node.mapData = node.left.mapData
                node.left.mapData = tell

        else:
            if node.left.data > node.right.data:
                if node.left.data > node.data:
                    temp = node.left.data
                    node.left.data = node.data
                    node.data = temp

                    tell = node.mapData
                    node.mapData = node.left.mapData
                    node.left.mapData = tell

                    if node.left:
                        self.adjustMax(node.left)
            else:
                if node.right.data > node.data:
                    temp = node.right.data
                    node.right.data = node.data
                    node.data = temp

                    tell = node.mapData
                    node.mapData = node.right.mapData
                    node.right.mapData = tell

                    if node.right:
                        self.adjustMax(node.right)

    # Display Queue
    def displayQueue(self):
        temp = self.root
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print("\n")


    # Display Queue with mapping
    def displayQueueDataWithMapping(self):
        temp = self.root
        while temp:
            print(f"{temp.data}--{temp.mapData}",end = " ")
            temp = temp.next
        print("\n")

    # Insertion of the node in MinQ
    def insertNodeInMinQueue(self,data,mappingData):
        aNode = priorityQueueNode(data)
        aNode.mapData = mappingData

        if not self.root:
            aNode.parent = None
            self.root = aNode
            self.insertPointNode = aNode
            self.lastNode = aNode

        else:
            if not self.insertPointNode.left:
                self.insertPointNode.left = aNode
                aNode.parent = self.insertPointNode
            elif not self.insertPointNode.right:
                self.insertPointNode.right = aNode
                aNode.parent = self.insertPointNode
                self.insertPointNode = self.insertPointNode.next
            else:
                pass
            self.lastNode.next = aNode
            aNode.back = self.lastNode
            self.lastNode = aNode
        self.adjustMinHeap(aNode)

    # Insertion of node in MaxQ
    def insertNodeInMaxQueue(self,data,mappingData):
        aNode = priorityQueueNode(data)
        aNode.mapData = mappingData

        if not self.root:
            aNode.parent = None
            self.root = aNode
            self.insertPointNode = aNode
            self.lastNode = aNode

        else:
            if not self.insertPointNode.left:
                self.insertPointNode.left = aNode
                aNode.parent = self.insertPointNode
            elif not self.insertPointNode.right:
                self.insertPointNode.right = aNode
                aNode.parent = self.insertPointNode
                self.insertPointNode = self.insertPointNode.next
            else:
                pass
            self.lastNode.next = aNode
            aNode.back = self.lastNode
            self.lastNode = aNode
        self.adjustMaxHeap(aNode)


    # Delete node from MaxHeap
    def deleteMaxNode(self):
        if self.root == self.lastNode:
            self.root = None
            self.insertPointNode = None
            self.lastNode = None
        else:
            if self.lastNode.parent.right:
                temp = self.lastNode.back
                self.root.data = self.lastNode.data
                self.root.mapData = self.lastNode.mapData
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.right = None
                self.lastNode.back.next = None
                self.lastNode = temp
            else:
                temp = self.lastNode.back
                self.root.data = self.lastNode.data
                self.root.mapData = self.lastNode.mapData
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.left = None
                self.lastNode.back.next = None
                self.lastNode = temp
        self.adjustMax(self.root)

    # Delete node from MinHeap
    def deleteMinNode(self):
        if self.root == self.lastNode:
            self.root = None
            self.insertPointNode = None
            self.lastNode = None
        else:
            if self.lastNode.parent.right:
                temp = self.lastNode.back
                self.root.data = self.lastNode.data
                self.root.mapData = self.lastNode.mapData
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.right = None
                self.lastNode.back.next = None
                self.lastNode = temp
            else:
                temp = self.lastNode.back
                self.root.data = self.lastNode.data
                self.root.mapData = self.lastNode.mapData
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.left = None
                self.lastNode.back.next = None
                self.lastNode = temp
        self.adjustMin(self.root)

    # Delete function to handel mapping data
    def deleteNodeFromDEminPQ(self):
        temp = self.root.mapData
        self.deleteMinNode()
        return temp

    # Arbitrary delete function
    def arbitraryDeleteInMax(self, data):
        # print("\n")
        temp = self.root
        while temp.data != data:
            temp = temp.next

        if temp.left == None and temp.right == None and self.root == self.lastNode:
            # print("Root condition match")
            # if self.root == self.lastNode:
            self.root = None
            self.insertPointNode = None
            self.lastNode = None

        elif temp == self.lastNode:
            if self.lastNode.parent.right == None:
                # print("Right node none!")
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.left = None
                self.lastNode.back.next = None
                self.lastNode = tell
            else:
                # print("Right node not none!")
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.right = None
                self.lastNode.back.next = None
                self.lastNode = tell
        elif temp.left != None and temp.right != None:
            # print("When both left and right node not none condition match!")
            temp.data = self.lastNode.data
            temp.mapData = self.lastNode.mapData
            if self.lastNode.parent.right == None:
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.left = None
                self.lastNode.back.next = None
                self.lastNode = tell
            else:
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.right = None
                self.lastNode.back.next = None
                self.lastNode = tell
            self.adjustMax(temp)
        elif temp.left != None and temp.right == None:
            # print("When left is not none but right is none")
            temp.data = self.lastNode.data
            temp.mapData = self.lastNode.mapData
            tell = self.lastNode.back
            self.insertPointNode = self.lastNode.parent
            self.lastNode.parent.left = None
            self.lastNode.back.next = None
            self.lastNode = tell
            # self.adjustMax(temp)
        else:
            # print("Elese condition match!")
            temp.data = self.lastNode.data
            temp.mapData = self.lastNode.mapData
            if self.lastNode.parent.right == None:
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.left = None
                self.lastNode.back.next = None
                self.lastNode = tell
            else:
                tell = self.lastNode.back
                self.insertPointNode = self.lastNode.parent
                self.lastNode.parent.right = None
                self.lastNode.back.next = None
                self.lastNode = tell



if __name__ == "__main__":
    minq = queueImplementation() # MinQ Object
    maxq = queueImplementation() # MaxQ Object

    buffer = [] # Buffer
    global_var = 0 # global variable to handel different file for creation and deletion
    gjob = []

    # Insert element in DEPQ
    def insertintoDEPQ(a): 
        if len(buffer) == 0:
            buffer.append(a)
        else:
            if buffer[0] > a:
                maxq.insertNodeInMaxQueue(buffer[0], a)
                minq.insertNodeInMinQueue(a, buffer[0])
            else:
                maxq.insertNodeInMaxQueue(a, buffer[0])
                minq.insertNodeInMinQueue(buffer[0], a)
            buffer.pop()

    # Delete minimum element in DEPQ
    def deleteminimumElementDEPQ():
        if len(buffer) == 0:
            # print(f"MQ data deleted: {minq.root.data}")
            gjob.append(minq.root.data)
            mapData = minq.deleteNodeFromDEminPQ()
            maxq.arbitraryDeleteInMax(mapData)
            buffer.append(mapData)
        else:
            # print(f"MQ data deleted: {minq.root.data}")
            if minq.root != None:
                if minq.root.data < buffer[0]:
                    # print(f"MQ data deleted: {minq.root.data}")
                    gjob.append(minq.root.data)
                    mapData = minq.deleteNodeFromDEminPQ()
                    maxq.arbitraryDeleteInMax(mapData)
                    insertintoDEPQ(mapData)
                else:
                    # print(f"MQ data deleted: {buffer[0]}")
                    gjob.append(buffer[0])
                    buffer.pop(0)


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

        os.remove(f"C:/Users/aashm/PycharmProjects/ComputerVision/{file3}")
        os.remove(f"C:/Users/aashm/PycharmProjects/ComputerVision/{file1}")

        return file2

    # Main funtion of external sorting
    def externalDataSorting(filename):
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


        num = len(bjob)
        if num <= 30:
            # print(f"Inside the small sorting!")
            while len(bjob):
                a = bjob.pop(0)
                insertintoDEPQ(a)

            for l in range(num - 1):
                deleteminimumElementDEPQ()
            gjob.append(buffer.pop(0))

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
            insertintoDEPQ(a)
        num = len(bjob)

        while(len(bjob)):
            a = bjob.pop(0)
            if a < minq.root.data:
                minDataList.append(a)
            elif a > maxq.root.data:
                maxDataList.append(a)
            else:
                minDataList.append(minq.root.data)
                deleteminimumElementDEPQ()
                insertintoDEPQ(a)


        while len(gjob):
            gjob.pop(0)


        for l in range(30):
            deleteminimumElementDEPQ()
        gjob.append(buffer.pop(0))


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
            externalDataSorting(f"newFileSmallerData{global_var}.txt")

    
        if number_of_element_large_list != 0:
            # print("function is called for Large data!")
            externalDataSorting(f"newFileLargerData{global_var}.txt")
        zjob = mergingFile(f"newFileSmallerData{global_var}.txt",filename,f"newFileLargerData{global_var}.txt")

        return zjob

    fileData = externalDataSorting("newFile.txt")
    # print(f"fileData value : {fileData}")

    displayData = open(fileData,"r")
    wjob = displayData.readlines()
    displayData.close()
    print(wjob)
