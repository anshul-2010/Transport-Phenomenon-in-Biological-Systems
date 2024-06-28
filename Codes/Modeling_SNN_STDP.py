import numpy as np
import matplotlib.pyplot as plt

# FitzHugh-Nagumo parameters
a = 0.7  # Excitability parameter
b = 0.8  # Inhibition parameter
tau = 12.5  # Time constant

# FitzHugh-Nagumo model
def fitzhugh_nagumo(v, w, I):
    dv = v - (v**3) / 3 - w + I
    dw = (v + a - b * w) / tau
    return dv, dw

# Simulation parameters
dt = 0.01  # Time step
T = 200  # Total simulation time
steps = int(T / dt)

# Neuron parameters
neurons = 50
neurons_in_first_layer = 100  # Number of neurons in the first layer
neurons_in_second_layer = 10  # Number of neurons in the second layer

# Neuron variables
v = np.random.rand(2, neurons_in_first_layer) * 2 - 1  # Two layers
w = np.random.rand(2, neurons_in_first_layer) * 2 - 1
spike_times = [[] for _ in range(2 * neurons_in_first_layer)]

# Synaptic weights and plasticity parameters
synaptic_weights = np.random.rand(neurons, neurons)
synaptic_strength = 0.2
learning_rate = 0.005

# Lists to store data
v_values = []
time_values = []

plt.figure(figsize=(12, 6))
plt.imshow(synaptic_weights, cmap='plasma', aspect='auto', origin='lower')
plt.colorbar()
plt.xlabel('Post-synaptic Neuron')
plt.ylabel('Pre-synaptic Neuron')
plt.title('Synaptic Weights')
plt.show()

# Simulate the SNN with STDP
for step in range(steps):
    time = step * dt
    time_values.append(time)
    v_values.append(v.copy())

    # Generate random spike events for input
    input_spikes = np.random.rand(neurons) < 0.01  # Random spikes

    # Apply external input to neurons based on spikes
    I_ext = np.dot(synaptic_weights, input_spikes) * synaptic_strength
    dv, dw = fitzhugh_nagumo(v, w, I_ext)
    v += dv * dt
    w += dw * dt

    # Update synaptic weights using STDP
    for pre_neuron in range(neurons):
        for post_neuron in range(neurons):
            if input_spikes[pre_neuron] and post_neuron != pre_neuron:
                if synaptic_weights[pre_neuron, post_neuron] > 0:
                    synaptic_weights[pre_neuron, post_neuron] -= learning_rate
                elif synaptic_weights[pre_neuron, post_neuron] < 0:
                    synaptic_weights[pre_neuron, post_neuron] += learning_rate

# Plot the membrane potentials of neurons and synaptic weights
v_values = np.array(v_values).T
plt.figure(figsize=(12, 6))
for i in range(neurons):
    plt.plot(time_values, v_values[i], label=f'Neuron {i}')
plt.xlabel('Time')
plt.ylabel('Membrane Potential')
plt.title('SNN with STDP Simulation')
plt.legend(loc='upper right')

plt.figure(figsize=(12, 6))
plt.imshow(synaptic_weights, cmap='plasma', aspect='auto', origin='lower')
plt.colorbar()
plt.xlabel('Post-synaptic Neuron')
plt.ylabel('Pre-synaptic Neuron')
plt.title('Synaptic Weights')
plt.show()