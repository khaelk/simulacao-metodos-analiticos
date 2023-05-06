from simulation import Simulation
from simpleQueue import SimpleQueue
from array import array
import configparser

#leitura do arquivo de configuracao
config = configparser.ConfigParser()
config.read("config.ini")
initialTime = int(config.get("configfile", "initialTime"))
quantityNums = int(config.get("configfile", "quantityNums"))
seed = int(config.get("configfile", "seed"))
#primeira fila
q1 = eval(config.get("configfile", "q1"))
#filas subsequentes
q2 = eval(config.get("configfile", "q2"))

queues = []

simQueue1 = SimpleQueue(q1[0], q1[1], q1[2], q1[3])
queues.append(simQueue1)

for q in q2:
    simQueue = SimpleQueue(q[0], q[1], -1, q[2])
    queues.append(simQueue)

#instanciacao e start da simulacao
sim = Simulation(initialTime, quantityNums, seed, simQueue1)
sim.execute()

#print de resultados
for index in range(len(sim.simQueue.timeAtService)):
    print(f'State: {index}, Time: {sim.simQueue.timeAtService[index]}, Probability: {round((sim.simQueue.timeAtService[index]/sim.time)*100,4)}%')
print("perdas: ",sim.losses)
input()