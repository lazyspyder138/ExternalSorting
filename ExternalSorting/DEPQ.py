
class TreeNode:
    def __init__(self ,data):
        self.val = data
        self.right = None
        self.left = None
        self.next =None
        self.parent = None
        self.previous = None
        self.correspondance = None


class Queue:
    def __init__(self):
        self.root = None
        self.insertptr = None
        self.lastptr = None

    def display(self):
        ptr = self.root
        while ptr != None:
            print(ptr.val, end=" ")
            ptr = ptr.next
        print()

    def minHeapify(self, ptr):
        if ptr == None or ptr.parent == None:
            return
        if ptr.val < ptr.parent.val:
            temp_val = ptr.val
            corresponce_node = ptr.correspondance
            ptr.val = ptr.parent.val
            ptr.correspondance = ptr.parent.correspondance
            ptr.parent.val = temp_val
            ptr.parent.correspondance = corresponce_node

            if ptr.parent:
                self.minHeapify(ptr.parent)

    def insertInMinHeap(self, value, mapping):
        node = TreeNode(value)
        node.correspondance = mapping

        if self.root == None:
            node.parent = None
            self.root = node
            self.insertptr = node
            self.lastptr = node

        else:
            if self.insertptr.left == None:
                self.insertptr.left = node
                node.parent = self.insertptr
            elif self.insertptr.right == None:
                self.insertptr.right = node
                node.parent = self.insertptr
                self.insertptr = self.insertptr.next
            else:
                pass
            self.lastptr.next = node
            node.previous = self.lastptr
            self.lastptr = node
        self.minHeapify(node)

    def displayCorrespondance(self):
        ptr = self.root
        while ptr != None:
            print(f"{ptr.val}--{ptr.correspondance}", end=" ")
            ptr = ptr.next
        print()

    def maxHeapify(self, ptr):
        if ptr == None or ptr.parent == None:
            return
        if ptr.val > ptr.parent.val:
            temp_val = ptr.val
            corresponce_node = ptr.correspondance
            ptr.val = ptr.parent.val
            ptr.correspondance = ptr.parent.correspondance
            ptr.parent.val = temp_val
            ptr.parent.correspondance = corresponce_node

            if ptr.parent:
                self.maxHeapify(ptr.parent)

    def insertInMaxHeap(self, value, mapping):
        node = TreeNode(value)
        node.correspondance = mapping

        if self.root == None:
            node.parent = None
            self.root = node
            self.insertptr = node
            self.lastptr = node

        else:
            if self.insertptr.left == None:
                self.insertptr.left = node
                node.parent = self.insertptr
            elif self.insertptr.right == None:
                self.insertptr.right = node
                node.parent = self.insertptr
                self.insertptr = self.insertptr.next
            else:
                pass
            self.lastptr.next = node
            node.previous = self.lastptr
            self.lastptr = node
        self.maxHeapify(node)

    def adjustMinHeap(self, ptr):
        if ptr == None or (ptr.left == None and ptr.right == None):
            return

        if ptr.left != None and ptr.right == None:
            if ptr.left.val < ptr.val:
                temp_correspondance = ptr.correspondance
                temp_val = ptr.val
                ptr.val = ptr.left.val
                ptr.correspondance = ptr.left.correspondance
                ptr.left.val = temp_val
                ptr.left.correspondance = temp_correspondance

        else:
            if ptr.left.val < ptr.right.val:
                if ptr.left.val < ptr.val:
                    temp_val = ptr.left.val
                    temp_correspondance = ptr.left.correspondance
                    ptr.left.val = ptr.val
                    ptr.left.correspondance = ptr.correspondance
                    ptr.val = temp_val
                    ptr.correspondance = temp_correspondance

                    if ptr.left:
                        self.adjustMinHeap(ptr.left)

            else:
                if ptr.right.val < ptr.val:
                    temp_val = ptr.right.val
                    temp_correspondance = ptr.right.correspondance
                    ptr.right.val = ptr.val
                    ptr.right.correspondance = ptr.correspondance
                    ptr.val = temp_val
                    ptr.correspondance = temp_correspondance

                    if ptr.right:
                        self.adjustMinHeap(ptr.right)

    def adjustMaxHeap(self, ptr):
        if ptr == None or (ptr.left == None and ptr.right == None):
            return
        if ptr.left != None and ptr.right == None:
            if ptr.left.val > ptr.val:
                temp_val = ptr.left.val
                temp_correspondance = ptr.left.correspondance
                ptr.left.val = ptr.val
                ptr.left.correspondance = ptr.correspondance
                ptr.val = temp_val
                ptr.correspondance = temp_correspondance

        else:
            if ptr.left.val > ptr.right.val:
                if ptr.left.val > ptr.val:
                    temp_val = ptr.left.val
                    temp_correspondance = ptr.left.correspondance
                    ptr.left.val = ptr.val
                    ptr.left.correspondance = ptr.correspondance
                    ptr.val = temp_val
                    ptr.correspondance = temp_correspondance

                    if ptr.left:
                        self.adjustMaxHeap(ptr.left)
            else:
                if ptr.right.val > ptr.val:
                    temp_val = ptr.right.val
                    temp_correspondance = ptr.right.correspondance
                    ptr.right.val = ptr.val
                    ptr.right.correspondance = ptr.correspondance
                    ptr.val = temp_val
                    ptr.correspondance = temp_correspondance

                    if ptr.right:
                        self.adjustMaxHeap(ptr.right)

    def deleteMax(self):
        if self.root == self.lastptr:
            self.root = None
            self.insertptr = None
            self.lastptr = None
        else:
            if self.lastptr.parent.right:
                temp = self.lastptr.previous
                self.root.val = self.lastptr.val
                self.root.correspondance = self.lastptr.correspondance
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.right = None
                self.lastptr.previour.next = None
                self.lastptr = temp
            else:
                temp = self.lastptr.previous
                self.root.val = self.lastptr.val
                self.root.correspondance = self.lastptr.correspondance
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.left = None
                self.lastptr.previous.next = None
                self.lastptr = temp

        self.adjustMaxHeap(self.root)

    def deleteMin(self):
        if self.root == self.lastptr:
            self.root = None
            self.insertptr = None
            self.lastptr = None
        else:
            if self.lastptr.parent.right:
                temp = self.lastptr.previous
                self.root.val = self.lastptr.val
                self.root.correspondance = self.lastptr.correspondance
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.right = None
                self.lastptr.previous.next = None
                self.lastptr = temp
            else:
                temp = self.lastptr.previous
                self.root.val = self.lastptr.val
                self.root.correspondance = self.lastptr.correspondance
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.left = None
                self.lastptr.previous.next = None
                self.lastptr = temp

        self.adjustMinHeap(self.root)

    def deleteFromMinHeap(self):
        temp = self.root.correspondance
        self.deleteMin()
        return temp

    def deleteElement(self, value):
        temp_node = self.root
        while temp_node.val != value:
            temp_node = temp_node.next

        if temp_node.left == None and temp_node.right == None and self.root == self.lastptr:
            self.root = None
            self.insertptr = None
            self.lastptr = None

        elif temp_node == self.lastptr:
            if self.lastptr.parent.right == None:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.left = None
                self.lastptr.previous.next = None
                self.lastptr = temp
            else:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.right = None
                self.lastptr.previous.next = None
                self.lastprevious = temp
        elif temp_node.left != None and temp_node.right != None:
            temp_node.val = self.lastptr.val
            temp_node.correspondance = self.lastptr.correspondance
            if self.lastptr.parent.right == None:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.left = None
                self.lastptr.previous.next = None
                self.lastptr = temp
            else:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.right = None
                self.lastptr.previous.next = None
                self.lastptr = temp
            self.adjustMaxHeap(temp_node)
        elif temp_node.left != None and temp_node.right == None:
            temp_node.val = self.lastptr.val
            temp_node.correspondance = self.lastptr.correspondance
            temp = self.lastptr.previous
            self.insertptr = self.lastptr.parent
            self.lastptr.parent.left = None
            self.lastptr.previous.next = None
            self.lastptr = temp
            # self.adjustMaxHeap(temp_node)
        else:
            temp_node.val = self.lastptr.val
            temp_node.correspondance = self.lastptr.correspondance
            if self.lastptr.parent.right == None:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.left = None
                self.lastptr.previous.next = None
                self.lastptr = temp
            else:
                temp = self.lastptr.previous
                self.insertptr = self.lastptr.parent
                self.lastptr.parent.right = None
                self.lastptr.previous.next = None
                self.lastptr = temp


class DoubleEndedQueue:

    def __init__(self):
        self.minq = Queue()
        self.maxq = Queue()
        self.buffer = []

    def insertintoDEPQ(self, a):
        if len(self.buffer) == 0:
            self.buffer.append(a)
        else:
            if self.buffer[0] > a:
                self.maxq.insertInMaxHeap(self.buffer[0], a)
                self.minq.insertInMinHeap(a, self.buffer[0])
            else:
                self.maxq.insertInMaxHeap(a, self.buffer[0])
                self.minq.insertInMinHeap(self.buffer[0], a)
            self.buffer.pop()

    def deleteminimumElementDEPQ(self):
        if len(self.buffer) == 0:
            mapData = self.minq.deleteFromMinHeap()
            self.maxq.deleteElement(mapData)
            self.buffer.append(mapData)
        else:
            if self.minq.root.val < self.buffer[0]:
                mapData = self.minq.deleteFromMinHeap()
                self.maxq.deleteElement(mapData)
                self.insertintoDEPQ(mapData)
            else:
                self.buffer.pop(0)


if __name__ == "__main__":
    Depq = DoubleEndedQueue()
    li = [12, 70, 8, 1, 11, 20, 4, 19, 7, 10, 6, 13]

    while len(li):
        data = li.pop(0)
        Depq.insertintoDEPQ(data)

    Depq.minq.display()

    Depq.maxq.display()

    Depq.minq.displayCorrespondance()

    Depq.maxq.displayCorrespondance()

    print(
        f"MinQ Root data - {Depq.minq.root.val}, Last data - {Depq.minq.lastptr.val},Root Map Data - {Depq.minq.root.correspondance}")

    print(
        f"MaxQ Root data - {Depq.maxq.root.val}, Last data - {Depq.maxq.lastptr.val},Root Map Data - {Depq.maxq.root.correspondance}")

    Depq.deleteminimumElementDEPQ()
    Depq.minq.display()
    Depq.maxq.display()
    Depq.minq.displayCorrespondance()
    Depq.maxq.displayCorrespondance()

    Depq.deleteminimumElementDEPQ()
    Depq.minq.display()
    Depq.maxq.display()
    Depq.minq.displayCorrespondance()
    Depq.maxq.displayCorrespondance()