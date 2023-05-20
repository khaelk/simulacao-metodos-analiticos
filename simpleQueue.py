class SimpleQueue:
    def __init__(self, index, servers, capacity, arrivalTime, serviceTime):
        self.index = index
        self.servers = servers
        self.capacity = capacity
        self.clients = 0 #num slots ocupados
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        self.timeAtService = [0] * (capacity+1)