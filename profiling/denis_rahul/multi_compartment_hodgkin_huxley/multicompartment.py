import numpy as np
from scipy.signal import argrelextrema

# Hodgkin-Huxley ion channel dynamics:
# We are using SI units, therefore the equations have been adapted to use v[V] as argument and return rate[1/s]
alpha_n = lambda v: ( 0.01*(v*1e3+55.)/(1-np.exp(-0.1*(v*1e3+55.))) ) * 1e3
beta_n = lambda v: ( 0.125*np.exp(-0.0125*(v*1e3+65.)) ) * 1e3

alpha_m = lambda v: ( 0.1*(v*1e3+40.)/(1-np.exp(-0.1*(v*1e3+40.))) ) * 1e3
beta_m = lambda v: ( 4*np.exp(-0.0556*(v*1e3+65.)) ) * 1e3

alpha_h = lambda v: ( 0.07*np.exp(-0.05*(v*1e3+65.)) ) * 1e3
beta_h = lambda v: ( 1/(1+np.exp(-0.1*(v*1e3+35.))) ) * 1e3
    

class MultiCompartmentHodgkinHuxley(object):
    """ Class to model an axon with a multi-compartment Hodgkin-Huxley model. All compartments are assumes
    to have same size."""

    def __init__(self, N, a=238e-6, L=1e-2, rL=35.4e-2, cm=1e-2, mu_inj=[1], Ie=[10e-9],
            v0=-65e-3, gL=0.3, gK=3.6e2, gNa=1.2e3, EL=-54.387e-3, EK=-77e-3, ENa=50e-3, z=0.5,
            myelinated=False, len_ranvier=2e-6, len_myelin=1e-3):

            """
            :param N: (int) number of compartments
            :param a: (scalar, default=238e-6) cable radius [m]
            :param L: (scalar, default=1e-2) total cable length [m]
            :param rL: (scalar, default=35.4e-2) intracellular resistivity [Ohm*m]
            :param cm: (scalar, default=1e-2) specific membrane capacitance [F/(m^2)]
            :param mu_inj: (array of int, default=[0]) compartment of current injection(s)
            :param Ie: (array of scalars, default=[10e-9]) total external current injected 
                        in compartments specified in mu_inj, len(mu_inj) must equal len(Ie) [A]
            :param v0: (scalar, default=-65e-3) initial membrane voltage [V]
            :param gL: (scalar, default=0.3) leak conductance [S/((m^2)]
            :param gK: (scalar, default=3.6e2) maximum conductance of potassium channel [S/(m^2)]
            :param gNa: (scalar, default=1.2e3) maximum conductance of sodium channel [S/(m^2)]
            :param EL: (scalar, default=-54.387e3) reversal potential of leakage [V]
            :param EK: (scalar, default=-77e-3) reversal potential of potassium channel [V]
            :param ENa: (scalar, default=50e-3) reversal potential of sodium channel [V]
            :param z: (scalar, default=0.5) z=0.5 is Crank-Nicholson, z=1 is reverse Euler method
            :param meyelinated: (bool, default=False) if True, the axon is split in blocks of myelinated compartement 
                        and rode of ranvier nodes
            :param len_ranvier: (scalar, default=2e-6) if myelinated==True: length of nodes of ranvier [m]
            :param len_myelin: (scalar, default=1e-3) if myelinated==True: length of myelinated parts [m]

            """

            assert len(mu_inj)==len(Ie), "Number of injection sides len(mu_inj) and number of current values len(Ie) are not equal!"

            self.a = a
            self.L = L
            self.rL = rL
            self.cm = cm
            self.Ie = np.array(Ie)
            self.mu_inj = np.array(mu_inj)
            self.N = N
            self.v0 = v0
            self.gL = gL
            self.gK = gK
            self.gNa = gNa
            self.EL = EL
            self.EK = EK
            self.ENa = ENa
            self.z = z
            self.myelinated = myelinated

            self.prev_cm = cm # hacky! for myelinated C and c calculation 

            # electronic length constant lambda
            self.l = np.sqrt( a / (2*rL* ( gL / (2 * np.pi * self.a * (self.L/self.N) * 1e-4)))) 
            # analytical spike propagation velocity
            self.anal_vel = np.sqrt(a/(2*cm**2*rL*(1./gL)))

            # suface area of compartments
            self.S = (2 * np.pi * self.a * self.L/self.N)
            # injected current per unit are [A/(m^2)], value given by scaled Ie for given injection positions, 0 else
            self.ie = np.zeros(self.N)
            self.ie[self.mu_inj] = self.Ie / self.S 

            # coupling constant for resistive coupling between compartments
            self.g_coupling = a/(2*rL*(L/N)**2) 

            # initialize gating variables for each compartment
            self.n = np.ones(self.N) * 0.3177
            self.m = np.ones(self.N) * 0.0529
            self.h = np.ones(self.N) * 0.5961
            
            # initialize delta V array
            self.dv = np.zeros((self.N)) 

            if myelinated:
                self.len_myelin = len_myelin
                self.len_ranvier = len_ranvier
                assert self.L/self.N <= len_ranvier, 'Compartement length ({} m) is smaller then length of nodes of Ranvier(2e-6 m).'.format(self.L/self.N)
                if L <= len_myelin: print('WARNING: The entire axon is myelinated! Increase axon sice if you want nodes of Ranvier!')
                
                # little complicated way of creating an boolean array specifying for each compartment if its myelinated [True] or not [False]
                # number of compartments per myelinated or ranvier part and per block (one ranvier + one ranvier part)
                num_per_ranvier = np.ceil((len_ranvier/(L/N)))
                num_per_myelin = np.ceil(len_myelin/(L/N))
                num_blocks = np.floor((N - np.floor(0.5*num_per_myelin)) / (num_per_myelin + num_per_ranvier))

                # start with myelinated compartments of size 0.5*len_myelin
                myelin_pos = [True]* int(0.5*num_per_myelin)
                # add as many nodes of ranvier and myelinated parts as fit in axon length
                myelin_pos += num_blocks * ([False]*num_per_ranvier + [True]*num_per_myelin)
                # fill up the left compartments as myelinated
                myelin_pos += (N-len(myelin_pos)) * [True]

                self.myelin_pos = np.array(myelin_pos, dtype=bool)
                assert N==len(myelin_pos), 'Length of myelin_pos != number of compartments! Fix it!'
                
                print('# ranvier', num_per_ranvier)
                print('# myelin', num_per_myelin)
                print('# blocks', num_blocks)
                print('size array', len(self.myelin_pos))
            else: # all compartments not myelinated
                self.myelin_pos = np.zeros(N)


    def solve_for_time_step(self, ti):
        """
        Solve the coupled set of linear differential equations (all compartments) for the membrane voltage for a single timestep.
        The steps described in Dayan and Abbott chapter 6.6B are implemented here with simplifications for same sized compartments.

        :param ti: (int) time index
        """

        self.b_prime = np.zeros(self.N)
        self.d_prime = np.zeros(self.N)

        # loop through all compartments to get d_prine and b_prime values
        for mu in range(0,self.N):

            if self.myelin_pos[mu]:
                # muelin decreases membrane capacitance and leak conductance
                cm = self.cm / 50.
                gL = self.gL / 5000.
                # no ion channels can be used when myelin is present
                gNa = 0
                gK = 0
            else:
                cm = self.cm
                gL = self.gL
                gNa = self.gNa
                gK = self.gK
            
            g_sum = (gL 
                    + gNa * self.m[mu]**3 * self.h[mu]
                    + gK * self.n[mu]**4)
            g_E_sum = (gL * self.EL 
                        + self.ENa * gNa * self.m[mu]**3 * self.h[mu]
                        + self.EK * gK * self.n[mu]**4)

            # update channel variables
            v_old = self.v[mu,ti-1]
            dndt = alpha_n(v_old) * (1. - self.n[mu]) - beta_n(v_old) * self.n[mu]
            dmdt = alpha_m(v_old) * (1. - self.m[mu]) - beta_m(v_old) * self.m[mu]
            dhdt = alpha_h(v_old) * (1. - self.h[mu]) - beta_h(v_old) * self.h[mu]
            self.m[mu] = self.m[mu] + dmdt * self.dt 
            self.h[mu] = self.h[mu] + dhdt * self.dt
            self.n[mu] = self.n[mu] + dndt * self.dt

            A = self.g_coupling / cm
            C = self.g_coupling / cm
            D = (self.ie[mu] + g_E_sum) / cm

            a = A * self.z * self.dt
            c = self.g_coupling / self.cm * self.z * self.dt
            c_prev = self.g_coupling / self.prev_cm * self.z * self.dt # hacky! using c from previous compartment for calc b_prime

            if mu==0: # first compartment a=0, g_coupling(-1,0)=0 and b'=b, d'=d
                B = - (self.g_coupling + g_sum) / cm 
                b = B * self.z * self.dt
                d = (D + B * self.v[mu,ti-1] + C * self.v[mu+1,ti-1]) * self.dt
                self.b_prime[mu] = b
                self.d_prime[mu] = d
            else :
                if mu==self.N-1: # last compartment c=0, g_coupling(N,N+1)=0
                    B = - (self.g_coupling + g_sum) / cm 
                    b = B * self.z * self.dt
                    d = (D + A * self.v[mu-1,ti-1] + B * self.v[mu,ti-1] ) * self.dt
                else:   
                    B = - (2*self.g_coupling + g_sum) / cm 
                    b = B * self.z * self.dt
                    d = (D + A * self.v[mu-1,ti-1] + B * self.v[mu,ti-1] + C * self.v[mu+1,ti-1]) * self.dt
                self.b_prime[mu] = b + (a * c) / (1 - self.b_prime[mu-1])
                self.d_prime[mu] = d + (a * self.d_prime[mu-1]) / (1 - self.b_prime[mu-1])

            self.prev_cm = cm # save cm for case of change btwn myelinated and not myelinated compartment for calc c_(mu-1) 
            
        # loop through the compartments in reversed order to get the Delta v values
        self.dv[-1] = self.d_prime[-1] / (1 - self.b_prime[-1])
        for mu in reversed(range(0,len(self.dv)-1)):
            self.dv[mu] = (c * self.dv[mu+1] + self.d_prime[mu]) / (1 - self.b_prime[mu])

        # update voltage of all compartments for given time step
        self.v[:,ti] = self.v[:,ti-1] + self.dv


    def solve(self, t, dt, a_array=np.array([])):
        """
        Solve Multi-Compartment Hodgkin-Huxley neuron for a runtime t with time step dt.

        :param t: (scalar) runtime
        :param dt: (scalar) time step
        :param a_array: (np.array, default empty) Values of axon radiuses a. For each a in 
                a_array the model is solved and the propagation velocity is saved
        """
        self.dt = dt
        time_steps = int(float(t)/dt)

        if a_array.size==0:
            self.v = np.zeros((self.N,time_steps)) # v[mu,t] gives voltage at compartment mu and time t
            self.v[:,0] = np.ones(self.N) * self.v0
            self.t = np.zeros(time_steps)
    
            for ti in range(1,time_steps):
                self.solve_for_time_step(ti)
                self.t[ti] = self.t[ti-1] + dt

        # the following was implemented but not used for plot generation in report! We used a outside the classe.
        else:
            self.vel = np.zeros(a_array.size)
            for i,a in enumerate(a_array):
                # reset initial values and arrays
                self.a = a
                self.v = np.zeros((self.N,time_steps)) # v[mu,t] gives voltage at compartment mu and time t
                self.v[:,0] = np.ones(self.N) * self.v0
                self.t = np.zeros(time_steps)
                self.S = (2 * np.pi * self.a * self.L/self.N)
                self.ie[self.mu_inj] = self.Ie / self.S 

                # coupling constant for resistive coupling between compartments
                self.g_coupling = self.a/(2*self.rL*(self.L/self.N)**2) 

                # initialize gating variables for each compartment
                self.n = np.ones(self.N) * 0.3177
                self.m = np.ones(self.N) * 0.0529
                self.h = np.ones(self.N) * 0.5961

                self.dv = np.zeros((self.N)) # v[mu,ti] gives voltage at compartment mu and time t
    
                for ti in range(1,time_steps):
                    self.solve_for_time_step(ti)
                    self.t[ti] = self.t[ti-1] + dt

                # TODO mu1 mu2 in argument function
                self.calculate_propagation_velocity(100,200)
                self.vel[i] = self.prop_velocity


    def find_peaks(self, mu1, mu2, thresh=0.):
        """ Find greater value between two inputs mu1, mu2. If inputs are below the threshold
            thresh, set them to very low value (-1000)
        """
        mu1[mu1<thresh] = -1000
        mu2[mu2<thresh] = -1000
        return np.greater(mu1,mu2)


    def calculate_propagation_velocity(self, mu1, mu2, n=0):
        """
        Calculate propagation velosity between the nth spikes of compartment mu1 and mu2
        """

        # get array of all local extrema using self.find_peaks function
        peaks1 = argrelextrema(self.v[mu1,:], self.find_peaks)[0]
        peaks2 = argrelextrema(self.v[mu2,:], self.find_peaks)[0]
        #print 'peaks1', peaks1.shape
        #print 'peaks2', peaks2.shape
        # in case of too less spiking, set velocity to 0
        if peaks1.size<=n or peaks2.size<=n:
            self.prop_velocity = 0
            return 0
        else:
            # get indices of peak positions
            idx1 = peaks1[n]
            idx2 = peaks2[n]
            delta_x = float((mu2-mu1)) * self.L/float(self.N)
            #print 'delta x', delta_x
            delta_t = self.t[idx2] - self.t[idx1]
            #print 'delta t', delta_t
            self.prop_velocity = delta_x/delta_t


    
