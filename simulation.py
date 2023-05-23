from randomGen import GeneratedNums
from simpleQueue import SimpleQueue

class Simulation:
    def __init__(self, initialTime, quantityNums, seed, simpleQueue1, simpleQueue2):
        self.time = 0
        self.initialEventTime = initialTime
        self.nums = GeneratedNums(quantityNums, seed)
        self.usedNums = 0
        self.quantityNums = quantityNums
        self.simQueue1 = simpleQueue1
        self.simQueue2 = simpleQueue2
        self.losses = 0
        self.scheduler = []
        self.events = []

    #funcao que consome o numero aleatorio para gerar o tempo para o evento no escalonador
    def convert(self, a, b):
        result = (b-a)*self.nums.getNums()[self.usedNums]+a
        self.usedNums+=1
        return result

    #funcao que escalona eventos/realiza sorteio
    def putSchedule(self, event):
        if self.usedNums>=self.quantityNums:
            return
        #sorteio
        if event == 'ch1':
            eventTime = round(self.convert(self.simQueue1.arrivalTime[0],self.simQueue1.arrivalTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': self.simQueue1.index}
        if event == 'p12':
            eventTime = round(self.convert(self.simQueue1.serviceTime[0], self.simQueue1.serviceTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': self.simQueue1.index}
        if event == 'sa2':
            eventTime = round(self.convert(self.simQueue2.serviceTime[0],self.simQueue2.serviceTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': self.simQueue2.index}
        self.scheduler.append(schedule)
        #ordena o escalonador
        self.scheduler = sorted(self.scheduler, key=lambda x: float(x['time']))

    #funcao de start da simulacao
    def execute(self):
        #primeira chegada escalonador
        firstSchedule = {'event': 'ch1', 'time': self.initialEventTime, 'queue': self.simQueue1.index}
        self.scheduler.append(firstSchedule)
        while(self.usedNums<self.quantityNums):
            #pega evento com 'menor tempo'
            event = self.scheduler.pop(0)
            print(event, end='\n\n')
            #contabiliza tempo
            #para cada fila contabilizar o tempo
            self.simQueue1.timeAtService[self.simQueue1.clients]=round(self.simQueue1.timeAtService[self.simQueue1.clients] + event.get('time')-self.time,4)
            self.simQueue2.timeAtService[self.simQueue2.clients]=round(self.simQueue2.timeAtService[self.simQueue2.clients] + event.get('time')-self.time,4)
            self.time = event.get('time')
            print("index:" + str(self.simQueue1.index) + str(self.simQueue1.timeAtService), end='\n\n')
            print("index:" + str(self.simQueue2.index) + str(self.simQueue2.timeAtService), end='\n\n')
            #print(self.time)
            if event.get('event') == 'ch1':
                self.ch1()
            if event.get('event') == 'p12':
                self.p12()
            if event.get('event') == 'sa2':
                self.sa2()

    #funcao de chegada na fila simples
    def ch1(self):
        if self.simQueue1.clients<self.simQueue1.capacity:
            self.simQueue1.clients+=1
            if self.simQueue1.clients<=self.simQueue1.servers:
                self.putSchedule('p12')#agenda tranferencia f1 para f2
        else:
            self.losses+=1
        self.putSchedule('ch1')#chegada
    
    #funcao de transferencia f1 para f2
    def p12(self):
        self.simQueue1.clients-=1
        if self.simQueue1.clients>=self.simQueue1.servers:
            self.putSchedule('p12')#transferencia f1 f2
        if self.simQueue2.clients<self.simQueue2.capacity:
            self.simQueue2.clients+=1
            if self.simQueue2.clients<=self.simQueue2.servers:
                self.putSchedule('sa2')#saida f2
        else:
            self.losses+=1

    #funcao de saida na fila simples
    def sa2(self):
        self.simQueue2.clients-=1
        if self.simQueue2.clients>=self.simQueue2.servers:
            self.putSchedule('sa2')#saida f2