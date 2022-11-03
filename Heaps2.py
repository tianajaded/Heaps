    def __str__(self):
        return str(self.heap_list[1:])

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index//2]:
                self.heap_list[index], self.heap_list[index //
                                                      2] = self.heap_list[index//2], self.heap_list[index]
            index = index // 2

    def percolate_down(self, index):
        while (index*2) <= self.size:
            max_child = self.max_child(index)
            if self.heap_list[index] < self.heap_list[max_child]:

                self.heap_list[index], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[index]
            index = max_child

    def del_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size-1
        self.percolate_down(1)
        return min_val

    def min_child(self, index):
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
            index -= 1

    def del_max(self):
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return val

    def max_child(self, index):
        if index*2 >= self.size:
            return index*2
        else:
            if self.heap_list[index*2] > self.heap_list[index*2+1]:
                return index*2
            return index*2+1


def main():
    A = BinaryMaxHeap()

    A.insert(3)
    A.insert(9)
    A.insert(2)
    A.insert(1)
    A.insert(4)
    A.insert(5)

    print(A)
    print(A.del_max())
    print(A)
    print(A.max_child(1))


main()
