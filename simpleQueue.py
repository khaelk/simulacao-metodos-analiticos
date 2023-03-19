class SimpleQueue:
    def __init__(self, arrivals, service, servers, capacity, arrivalTime, serviceTime):
        self.arrivals = arrivals
        self.service = service
        self.servers = servers
        self.capacity = capacity
        self.clients = 0 #num slots ocupados
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime