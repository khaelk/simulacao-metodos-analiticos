from randomGen import GeneratedNums
from simpleQueue import SimpleQueue

class Simulation:
    def __init__(self, initialTime, quantityNums, arrivals, service, servers, capacity, arrivalTime, serviceTime):
        self.time = 0
        self.lastEventTime = initialTime
        self.nums = GeneratedNums(quantityNums)
        self.usedNums = 0
        self.quantityNums = quantityNums
        self.simQueue = SimpleQueue(arrivals, service, servers, capacity, arrivalTime, serviceTime)
        self.scheduler = []
        self.events = []

    def convert(self, a, b):
        result = (b-a)*self.nums.getNums()[self.usedNums]+a
        self.usedNums+=1
        return result

    def putSchedule(self, q, event):
        #sorteio
        if event == 'c':
            eventTime = self.convert(q.arrivalTime[0],q.arrivalTime[1])
        if event == 's':
            eventTime = self.convert(q.serviceTime[0],q.serviceTime[1])
        #guarda eventos no escalonador
        schedule = {'event': event, 'time': eventTime}
        self.scheduler.append(schedule)

    def execute(self):
        self.putSchedule(self.simQueue, 'c')
        while(self.usedNums<self.quantityNums):
            event = self.scheduler.pop()
            print(event)
            break

    def arrive(self):
        #contabiliza tempo
        if self.simQueue.clients<capacity:
            self.simQueue.clients+=1
            if self.simQueue.clients<=servers:
                self.putSchedule(self.simQueue, 's')#saida
        self.putSchedule(self.simQueue, 'c')#chegada

    def served(self):
        #contabiliza tempo
        self.simQueue.clients-=1
        if self.simQueue.clients>=servers:
            self.putSchedule(self.simQueue, 's')#saida