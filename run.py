from simulation import Simulation
from array import array
import configparser

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

sim = Simulation(initialTime, quantityNums, seed, arrivals, service, servers, capacity, arrivalTime, serviceTime)
sim.execute()
print("perdas: ",sim.losses)