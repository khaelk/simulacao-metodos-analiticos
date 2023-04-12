from randomGen import GeneratedNums
from simpleQueue import SimpleQueue

class Simulation:
    def __init__(self, initialTime, quantityNums, seed, arrivals, service, servers, capacity, arrivalTime, serviceTime):
        self.time = 0
        self.initialEventTime = initialTime
        self.nums = GeneratedNums(quantityNums, seed)
        self.usedNums = 0
        self.quantityNums = quantityNums
        self.simQueue = SimpleQueue(arrivals, service, servers, capacity, arrivalTime, serviceTime)
        self.losses = 0
        self.scheduler = []
        self.events = []

    #funcao que consome o numero aleatorio para gerar o tempo para o evento no escalonador
    def convert(self, a, b):
        result = (b-a)*self.nums.getNums()[self.usedNums]+a
        self.usedNums+=1
        return result

    #funcao que escalona eventos/realiza sorteio
    def putSchedule(self, q, event):
        #sorteio
        if event == 'c':
            eventTime = round(self.convert(q.arrivalTime[0],q.arrivalTime[1]) + self.time,4)
        if event == 's':
            eventTime = round(self.convert(q.serviceTime[0],q.serviceTime[1]) + self.time,4)
        #guarda eventos no escalonador
        schedule = {'event': event, 'time': eventTime}
        self.scheduler.append(schedule)
        #ordena o escalonador
        self.scheduler = sorted(self.scheduler, key=lambda x: float(x['time']))

    #funcao de start da simulacao
    def execute(self):
        #primeira chegada escalonador
        firstSchedule = {'event': 'c', 'time': self.initialEventTime}
        self.scheduler.append(firstSchedule)
        while(self.usedNums<self.quantityNums):
            #pega evento com 'menor tempo'
            event = self.scheduler.pop(0)
            print(event, end=' ')
            #contabiliza tempo
            self.simQueue.timeAtService[self.simQueue.clients]=round(self.simQueue.timeAtService[self.simQueue.clients] + event.get('time')-self.time,4)
            self.time = event.get('time')
            print(self.simQueue.timeAtService, end='\n\n')
            #print(self.time)
            if event.get('event') == 'c':
                self.arrive()
            if event.get('event') == 's':
                self.served()
            #debugging dos eventos
            #self.events.append(event)
            #print(self.events)
            #break

    #funcao de chegada na fila simples
    def arrive(self):
        if self.simQueue.clients<self.simQueue.capacity:
            self.simQueue.clients+=1
            if self.simQueue.clients<=self.simQueue.servers:
                self.putSchedule(self.simQueue, 's')#saida
        else:
            self.losses+=1
        self.putSchedule(self.simQueue, 'c')#chegada

    #funcao de saida na fila simples
    def served(self):
        self.simQueue.clients-=1
        if self.simQueue.clients>=self.simQueue.servers:
            self.putSchedule(self.simQueue, 's')#saida