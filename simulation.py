from randomGen import GeneratedNums
from simpleQueue import SimpleQueue

class Simulation:
    def __init__(self, initialTime, quantityNums, seed, queuesList):
        self.time = 0
        self.initialEventTime = initialTime
        self.nums = GeneratedNums(quantityNums, seed)
        self.usedNums = 0
        self.quantityNums = quantityNums
        self.queuesList = queuesList
        self.losses = 0
        self.scheduler = []
        self.events = []

    #funcao que consome o numero aleatorio para gerar o tempo para o evento no escalonador
    def convert(self, a, b):
        result = (b-a)*self.nums.getNums()[self.usedNums]+a
        self.usedNums+=1
        return result

    #funcao que escalona eventos/realiza sorteio
    def putSchedule(self, event, q1, q2):
        if self.usedNums>=self.quantityNums:
            return
        #sorteio
        if event == 'ch1':
            eventTime = round(self.convert(q1.arrivalTime[0],q1.arrivalTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': q1}
        if event == 'p12':
            eventTime = round(self.convert(q1.serviceTime[0], q1.serviceTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue1': q1, 'queue2': q2}
        if event == 'sa2':
            eventTime = round(self.convert(q1.serviceTime[0],q1.serviceTime[1]) + self.time,4)
            schedule = {'event': event, 'time': eventTime, 'queue': q1}
        self.scheduler.append(schedule)
        #ordena o escalonador
        self.scheduler = sorted(self.scheduler, key=lambda x: float(x['time']))

    #funcao de start da simulacao
    def execute(self):
        #primeiras chegadas escalonador
        for queue in self.queuesList:
            for time in self.initialEventTime:
                if time[0] == queue.name:
                    #firstArrival = round(self.convert(queue.arrivalTime[0],queue.arrivalTime[1]) + self.time,4)
                    firstSchedule = {'event': 'ch1', 'time': time[1], 'queue': queue}
                    self.scheduler.append(firstSchedule)
        while(self.usedNums<self.quantityNums):
            #print(self.scheduler)
            #pega evento com 'menor tempo'
            event = self.scheduler.pop(0)
            #print(event, end='\n\n')
            e = 'event'
            tm = 'time'
            qe1='queue1'
            qe2='queue2'
            qe='queue'
            if event.get('event') == 'p12':
                print(f'event: {event.get(e)}, time: {event.get(tm)}, queue1: {event.get(qe1).name}, queue2: {event.get(qe2).name}, {event.get(qe1).clients}, {event.get(qe2).clients}', end='\n\n')
            else:
                print(f'event: {event.get(e)}, time: {event.get(tm)}, queue: {event.get(qe).name}, {event.get(qe).clients}', end='\n\n')
            #contabiliza tempo
            #para cada fila contabilizar o tempo
            for queue in self.queuesList:
                queue.timeAtService[queue.clients]=round(queue.timeAtService[queue.clients] + event.get('time')-self.time,4)
                if len(queue.timeAtService)<=30:
                    print("name:" + queue.name + str(queue.timeAtService), end='\n\n')
                else:
                    print("name:" + queue.name + str(queue.timeAtService[:30]) + '...', end='\n\n')

            self.time = event.get('time')
            #print(self.time)
            if event.get('event') == 'ch1':
                self.ch1(event.get('queue'))
            if event.get('event') == 'p12':
                self.p12(event.get('queue1'), event.get('queue2'))
            if event.get('event') == 'sa2':
                self.sa2(event.get('queue'))

    def checkDestination(self, q, prob):
        for dest in q.network:
            if prob <= dest[1]:
                return dest[0]
            prob -= dest[1]
        return

    #funcao de chegada na fila
    def ch1(self, q):
        if q.clients<q.capacity:
            q.clients+=1
            if q.clients<=q.servers:
                dest = self.checkDestination(q, self.convert(0,1))
                if dest == 's':
                    self.putSchedule('sa2', q, -1)#agenda saida do sistema
                else:
                    q2 = ''
                    for q0 in self.queuesList:
                        if q0.name == dest:
                            q2 = q0
                    self.putSchedule('p12', q, q2)#agenda tranferencia f1 para f2
        else:
            self.losses+=1
            q.losses+=1
        self.putSchedule('ch1', q, -1)#chegada
    
    #funcao de transferencia
    def p12(self, q1 , q2):
        q1.clients-=1
        if q1.clients>=q1.servers:
            dest = self.checkDestination(q1, self.convert(0,1))
            #se dest = saida
            if dest == 's':
                self.putSchedule('sa2', q1, -1)#agenda saida do sistema
            #se dest = transferencia
            else:
                q2 = ''
                for q0 in self.queuesList:
                    if q0.name == dest:
                        q2 = q0
                self.putSchedule('p12', q1, q2)#agenda tranferencia f1 para f2
        if q2.clients<q2.capacity:
            q2.clients+=1
            if q2.clients<=q2.servers:
                self.putSchedule('sa2', q2, -1)#saida f2
        else:
            self.losses+=1
            q2.losses+=1

    #funcao de saida na fila
    def sa2(self, q):
        q.clients-=1
        if q.clients>=q.servers:
            self.putSchedule('sa2', q, -1)#saida f2