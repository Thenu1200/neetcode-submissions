class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = [0] * capacity


    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if (self.capacity <= self.size):
            self.resize()
        self.set(self.size, n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.get(self.size)


    def resize(self) -> None:
        self.data.extend([0] * self.capacity)
        self.capacity *= 2



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
