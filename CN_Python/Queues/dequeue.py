from sys import stdin
class Dequeue:
    def __init__(self):
        self.queue = []
        self.size = 0
        self.capacity = 10

    def insertFront(self, data):
        if self.size >= self.capacity:
            print(-1)
        else:
            self.queue.insert(0, data)
            self.size += 1

    def insertRear(self, data):
        if self.size >= self.capacity:
            print(-1)
        else:
            self.queue.append(data)
            self.size += 1

    def deleteFront(self):
        if self.size == 0:
            print(-1)
        else:
            self.queue.pop(0)
            self.size -= 1

    def deleteRear(self):
        if self.size == 0:
            print(-1)
        else:
            self.queue.pop()
            self.size -= 1

    def getFront(self):
        if self.size == 0:
            print(-1)
        else:
            print(self.queue[0])

    def getRear(self):
        if self.size == 0:
            print(-1)
        else:
            print(self.queue[-1])

# Read and process input
dq = Dequeue()
inputs=stdin.readline().strip().split(" ")
i=0
while True:
    
    choice = inputs[i]
    choice=int(choice)
    if choice == -1:
        break
    if choice == 1:
        data = inputs[i+1]
        i+=1
        dq.insertFront(data)
    elif choice == 2:
        data = inputs[i+1]
        i+=1
        dq.insertRear(data)
    elif choice == 3:
        dq.deleteFront()
    elif choice == 4:
        dq.deleteRear()
    elif choice == 5:
        dq.getFront()
    elif choice == 6:
        dq.getRear()
    i+=1
