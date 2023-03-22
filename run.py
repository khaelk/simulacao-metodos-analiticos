from simulation import Simulation

sim = Simulation(2, 10, 'G', 'G', 1, 3, [1,2], [3,6])
sim.execute()
print("perdas: ",sim.losses)