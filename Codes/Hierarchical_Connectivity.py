import numpy as np
import matplotlib.pyplot as plt

# Define FitzHugh-Nagumo neuron parameters
a = 0.7
b = 0.8
tau = 12.5
threshold = 1.0

# Simulation parameters
dt = 0.01
T = 100
steps = int(T / dt)
neurons_in_first_layer = 100  # Number of neurons in the first layer
neurons_in_second_layer = 10  # Number of neurons in the second layer

# Neuron variables
v = np.random.rand(2, neurons_in_first_layer) * 2 - 1  # Two layers
w = np.random.rand(2, neurons_in_first_layer) * 2 - 1
spike_times = [[] for _ in range(2 * neurons_in_first_layer)]

# Define hierarchical connectivity
synaptic_weights = np.zeros((neurons_in_first_layer, neurons_in_second_layer))

# Connect each neuron in the first layer to one neuron in the second layer
for i in range(neurons_in_first_layer):
    synaptic_weights[i, i % neurons_in_second_layer] = 1.0

# Input to Neurons
# For simplicity, we'll provide random input currents to neurons in the first layer
input_currents = np.random.uniform(0, 0.5, neurons_in_first_layer)

# Simulate the SNN and record spike times
for step in range(steps):
    I_ext = np.zeros((2, neurons_in_first_layer))  # Create a 2D array for input currents
    I_ext[0, :] = input_currents  # Neurons in the first layer receive input currents

    dv = (v - (v ** 3) / 3 - w + I_ext) / tau
    dw = (v + a - b * w) / tau
    v += dv * dt
    w += dw * dt

    for layer in range(2):
        for i in range(neurons_in_first_layer):
            if v[layer, i] >= threshold:
                spike_times[layer * neurons_in_first_layer + i].append(step * dt)
                v[layer, i] = -1.0
                w[layer, i] += 0.5

# Visualize spike times
plt.figure(figsize=(12, 6))
for i in range(2 * neurons_in_first_layer):
    plt.plot(spike_times[i], [i] * len(spike_times[i]), '*', markersize=10)
plt.xlabel('Time (s)')
plt.ylabel('Neuron Index')
plt.title('Spike Timing of Neurons in Two Layers (Hierarchical Connectivity)')
plt.show()