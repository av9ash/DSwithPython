CAPACITY = 16


class Heap(object):

    def __init__(self):
        self.heap = [0]*CAPACITY
        self.heap_size = 0

    def insert(self, value):
        self.heap[self.heap_size] = value
        self.heap_size += 1
        self.__settle_up__(self.heap_size-1)

    def __settle_up__(self, index):
        # root = i , left child = 2i+1, right child = 2i+2
        parent_index = (index-1)//2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.__swap__(index, parent_index)
            self.__settle_up__(parent_index)

    def __swap__(self, index, parent_index):
        self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

    def get_max(self):
        return self.heap[0]

    def pop_max(self):
        mx = self.get_max()
        self.__swap__(0,self.heap_size-1)
        del(self.heap[self.heap_size - 1])
        self.heap_size -= 1
        self.__settle_down__(0)
        return mx

    def __settle_down__(self, root_index):
        left_child_index = 2*root_index+1
        right_child_index = 2*root_index+2
        index_max = root_index

        if left_child_index < self.heap_size and self.heap[left_child_index] > self.heap[index_max]:
            index_max = left_child_index

        if right_child_index < self.heap_size and self.heap[right_child_index] > self.heap[index_max]:
            index_max = right_child_index

        if index_max != root_index:
            self.__swap__(root_index,index_max)
            self.__settle_down__(index_max)

    def heap_sort(self):
        size = self.heap_size
        for i in range(0, size):
            mx = self.pop_max()
            print(mx)


def main():
    h = Heap()

    for i in range(1,17):
        h.insert(i)

    h.heap_sort()


if __name__ == '__main__':
    main()

