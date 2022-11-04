

class BinaryMaxHeap():
    def __init__(self):
        '''initialize variables'''
        self.heap_list = [0]
        self.size = 0

    def __str__(self):
        '''function to return heap as strings'''
        return str(self.heap_list[1:])

    def is_empty(self):
        '''a function to check if the heap is empty'''
        return self.size == 0

    def insert(self, item):
        '''a function to insert an item into the heap'''
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, index):
        '''a function to move the max item up the chain to its correct position at the top of the heap'''
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index//2]:
                self.heap_list[index], self.heap_list[index //
                                                      2] = self.heap_list[index//2], self.heap_list[index]
            index = index // 2

    def percolate_down(self, index):
        '''a function to move the min item down to the bottom of the heap'''
        while (index*2) <= self.size:
            max_child = self.max_child(index)
            if self.heap_list[index] < self.heap_list[max_child]:

                self.heap_list[index], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[index]
            index = max_child

    def del_min(self):
        '''function to delete the minimum value in the heap'''
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size-1
        self.percolate_down(1)
        return min_val

    def min_child(self, index):
        '''function to compare the siblings if there's more than one child and returns whichever one is the min'''
        if index*2+1 > self.size:
            return index*2
        else:
            if self.heap_list[index*2] < self.heap_list[index*2+1]:
                return index*2
            else:
                return index*2+1

    def build_heap(self, alist):
        index = len(alist)//2  # any point past halfway point are leaves
        self.size = len(alist)
        self.heap_list = [0]+alist[:]
        while(index > 0):
            self.percolate_down(index)
            index += 1
        

    def del_max(self):
        '''function to delete the max value in the heap'''
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return val

    def max_child(self, index):
        '''function that compares the children and returns whichever one is the max'''
        if index*2 >= self.size:
            return index*2
        else:
            if self.heap_list[index*2] > self.heap_list[index*2+1]:
                return index*2
            return index*2+1

    def find_max(self):
        '''a function to find the max value in the heap'''
        if self.size > 0:
            min_val = self.heap_list[1]
            return min_val
        return None
    
    def remove(self, item):
        if item <= self.size:
            self.heap_list[item]=float("inf")
            self.percolate_up(item)
            self.del_max()
           





def main():
    A = BinaryMaxHeap()
    list = [5,53,21,36,35,4]
    build_heap(list)
 
    A.insert(5)
    A.insert(9)
    A.insert(11)
    A.insert(1)
    A.insert(3)
    A.insert(15)

    print(A)
    print(A.del_max())
    print(A)
    print(A.find_max())
    print(A)
    print(A.is_empty())
    A.insert(53)
    print(A)
    A.del_max()
    print(A)
    A.remove(9)
    print(A)


main()
