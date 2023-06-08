class SimpleQueue:
    def __init__(self, name, servers, capacity, arrivalTime, serviceTime, network):
        self.name = name
        self.servers = servers
        self.capacity = capacity
        self.clients = 0 #num slots ocupados
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        self.timeAtService = [0] * (capacity+1)
        self.losses = 0
        self.network = network