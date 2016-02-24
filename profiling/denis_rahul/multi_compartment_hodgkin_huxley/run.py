from multicompartment import MultiCompartmentHodgkinHuxley
import numpy as np

m = MultiCompartmentHodgkinHuxley(N=201, Ie=[2e-6], mu_inj=[0], L=3e-2)
m.solve(t=0.2, dt=0.00005)


