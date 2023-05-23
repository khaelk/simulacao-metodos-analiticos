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
#segunda fila
q2 = eval(config.get("configfile", "q2"))

simQueue1 = SimpleQueue(1, q1[0], q1[1], q1[2], q1[3])
simQueue2 = SimpleQueue(2, q2[0], q2[1], -1, q2[2])

#instanciacao e start da simulacao
sim = Simulation(initialTime, quantityNums, seed, simQueue1, simQueue2)
sim.execute()

#print de resultados
print('PROBABILIDADES DE ESTADO FILA 1')
for index in range(len(sim.simQueue1.timeAtService)):
    print(f'State: {index}, Time: {sim.simQueue1.timeAtService[index]}, Probability: {round((sim.simQueue1.timeAtService[index]/sim.time)*100,4)}%')
print('PROBABILIDADES DE ESTADO FILA 2')
for index in range(len(sim.simQueue2.timeAtService)):
    print(f'State: {index}, Time: {sim.simQueue2.timeAtService[index]}, Probability: {round((sim.simQueue2.timeAtService[index]/sim.time)*100,4)}%')
print("tempo simulacao: "+str(sim.time)+'s')
print("perdas: ",sim.losses)
input()