from randomGen import GeneratedNums
from simpleQueue import SimpleQueue

class Simulation:
    def __init__(self, initialTime, quantityNums, arrivals, service, servers, capacity, arrivalTime, serviceTime):
        self.time = 0
        self.lastEventTime = initialTime
        self.nums = GeneratedNums(quantityNums)
        self.usedNums = 0
        self.simQueue = SimpleQueue(arrivals, service, servers, capacity)
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        self.scheduler
        self.events

    def execute():
        return

    def arrive():
        #contabiliza tempo
        if self.simQueue.clients<capacity:
            self.simQueue.clients+=1
            if self.simQueue.clients<=servers:
                putSchedule()#saida
        putSchedule()#chegada

    def served():
        #contabiliza tempo
        self.simQueue.clients-=1
        if self.simQueue.clients>=servers:
            putSchedule()#saida

    def putSchedule():
        return

    def convert(a, b):
        result = (b-a)*nums[self.usedNums]+a
        self.usedNums+=1
        return result