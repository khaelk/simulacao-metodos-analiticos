from simulation import Simulation
from array import array
import configparser

#leitura do arquivo de configuracao
config = configparser.ConfigParser()
config.read("config.ini")
initialTime = int(config.get("configfile", "initialTime"))
quantityNums = int(config.get("configfile", "quantityNums"))
seed = int(config.get("configfile", "seed"))
arrivals = config.get("configfile", "arrivals")
service = config.get("configfile", "service")
servers = int(config.get("configfile", "servers"))
capacity = int(config.get("configfile", "capacity"))
arrivalTime = eval(config.get("configfile", "arrivalTime"))
serviceTime = eval(config.get("configfile", "serviceTime"))

#instanciacao e start da simulacao
sim = Simulation(initialTime, quantityNums, seed, arrivals, service, servers, capacity, arrivalTime, serviceTime)
sim.execute()

#print de resultados
for index in range(len(sim.simQueue.timeAtService)):
    print(f'State: {index}, Time: {sim.simQueue.timeAtService[index]}, Probability: {round((sim.simQueue.timeAtService[index]/sim.time)*100,4)}%')
print("perdas: ",sim.losses)
input()