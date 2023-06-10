from simulation import Simulation
from simpleQueue import SimpleQueue
from array import array
import configparser

inf = 999999

#leitura do arquivo de configuracao
config = configparser.ConfigParser()
config.read("config.ini")
initialTime = eval(config.get("configfile", "initialTime"))
quantityNums = int(config.get("configfile", "quantityNums"))
seed = int(config.get("configfile", "seed"))
#get filas
queuesListArr = eval(config.get("configfile", "queuesList"))
queuesListObj = []

for q in queuesListArr:
    simQueue = SimpleQueue(q[0], q[1], q[2], q[3], q[4], q[5])
    queuesListObj.append(simQueue)


#instanciacao e start da simulacao
sim = Simulation(initialTime, quantityNums, seed, queuesListObj, -1, -1)
sim.execute()

for queue in sim.queuesList:
    print(f'Queue: {queue.name}')
    limiter = 0
    for index in range(len(queue.timeAtService)):
        if limiter < 30:        
            print(f'State: {index}, Time: {queue.timeAtService[index]}, Probability: {round((queue.timeAtService[index]/sim.time)*100,4)}%')
        else:
            break
        limiter += 1
    print(f'Losses: {queue.losses}')
print(f'Tempo simulacao: {sim.time}')
print(f'Perdas totais: {sim.losses}')
#input()