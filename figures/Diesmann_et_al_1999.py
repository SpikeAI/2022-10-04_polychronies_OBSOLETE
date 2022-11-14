#!/usr/bin/env python
"""
Synfire chains
--------------
M. Diesmann et al. (1999). Stable propagation of synchronous spiking in cortical
neural networks. Nature 402, 529-533.
"""
from brian2 import *

duration = 100*ms

# Neuron model parameters
Vr = -70*mV
Vt = -55*mV
taum = 10*ms
taupsp = 0.325*ms
# weight = 4.86*mV
weight = 4.10*mV
# Neuron model
eqs = Equations('''
dV/dt = (-(V-Vr)+x)*(1./taum) : volt
dx/dt = (-x+y)*(1./taupsp) : volt
dy/dt = -y*(1./taupsp)+25.27*mV/ms+
        (39.24*mV/ms**0.5)*xi : volt
''')

# Neuron groups
n_groups = 10
group_size = 100
P = NeuronGroup(N=n_groups*group_size, model=eqs,
                threshold='V>Vt', reset='V=Vr', refractory=1*ms,
                method='euler')

N_inputs = 100
N_pulses = 5
spike_times = np.zeros(0)
np.random.seed(42)
for i_pulse in range(N_pulses):
        pulse = .5 * (N_pulses-i_pulse) * np.random.randn(N_inputs) + 10 + i_pulse*20
        spike_times = np.concatenate((spike_times, pulse))

spike_times = np.mod(spike_times, 100)

Pinput = SpikeGeneratorGroup(N_inputs*N_pulses, 
                            np.arange(N_inputs*N_pulses), 
                            spike_times*1*ms)
                             
                             
# The network structure
S = Synapses(P, P, on_pre='y+=weight')
S.connect(j='k for k in range((int(i/group_size)+1)*group_size, (int(i/group_size)+2)*group_size) '
            'if i<N_pre-group_size')
Sinput = Synapses(Pinput, P[:group_size], on_pre='y+=weight')
Sinput.connect()

# Record the spikes
Mgp = SpikeMonitor(P)
Minput = SpikeMonitor(Pinput)
# Setup the network, and run it
P.V = 'Vr + rand() * (Vt - Vr)'
run(duration)

# figure(figsize=(13, 8))
figure(figsize=(13, 5))
plot(Mgp.t/ms, 1.0*Mgp.i/group_size, '.')
plot([0, duration/ms], np.arange(n_groups).repeat(2).reshape(-1, 2).T, 'k-')
ylabel('group number')
yticks(np.arange(n_groups)+.5, labels=range(1, n_groups+1))

xlabel('time (ms)')
if True:
        show()
else:
        fname = 'Diesmann_et_al_1999'
        import matplotlib.pyplot as plt
        plt.savefig(fname + '.pdf', bbox_inches='tight', pad_inches=0.0, backend='pdf')
        #plt.savefig(fname + '.png', bbox_inches='tight', pad_inches=0.0, dpi=150, backend='agg')