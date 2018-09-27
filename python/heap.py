
# python has implementation for heap already which modifies the list in place, just like sort(), called heapq()
# Reference: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# Heaps where the parent key is greater than or equal to the child keys are called max-heaps; those where it is less than or equal to are called min-heaps

class Heap:
    def __init__(self, x):        
        """
        initialize with a list
        """
        self.elements = x
        self._heapify()
        
        
    def push(self, x):
        """
        adds element in order
        """
        self.elements.append(x)
        self._heapify()
    
    
    def pop(self):
        """
        removes smallest element i.e. first element from the list, and returns the value
        """
        temp = self.elements.pop(0)
        self._heapify()
        return temp
    
        
    def remove(self, v):
        """
        removes element matching the value
        """
        if v in self.elements:
            del self.elements[self.elements.index(v)]
            self._heapify()
        
        
    def _heapify(self):
        """
        cleans up the heap by replacing if the parent element is smaller than child
        """
        for _ in range(len(self.elements)):
            for i in range(len(self.elements)-1, 0, -1):
                if i%2 == 0:
                    parentPosition = (i-2)/2
                else:
                    parentPosition = (i-1)/2
                if parentPosition < 0:
                    parentPosition = 0
                
                # change this condition to '>' if coding for max-heap. This is for min-heap.
                if self.elements[i] < self.elements[parentPosition]:
                    self.elements[i], self.elements[parentPosition] = self.elements[parentPosition], self.elements[i]
                         
                                
if __name__ == '__main__':
    ip_list = [6, 7, 9, 4, 3, 5, 8, 10, 1] 
    print ip_list
    
    h = Heap(ip_list)
    print ip_list
    
    print h.pop()
    print ip_list
                
    h.push(11)       
    print ip_list
    h.push(1)
    print ip_list
    
    h.remove(3)
    print ip_list
