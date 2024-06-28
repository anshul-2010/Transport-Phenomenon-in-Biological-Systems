import numpy as np
from Mass_Flux_Matrix import mass_flux
import matplotlib.pyplot as plt

# Load your mass flux matrix (mass_flux) here

# Calculate the cumulative mass flux
cumulative_mass_flux = np.cumsum(mass_flux, axis=0)

# Normalize the cumulative mass flux
normalized_concentration = cumulative_mass_flux / mass_flux.shape[0]

# Plot concentration vs. time for each neuron in the second layer
plt.figure(figsize=(10, 6))
for neuron_index in range(normalized_concentration.shape[1]):
    plt.plot(np.arange(0, normalized_concentration.shape[0]), normalized_concentration[:, neuron_index], label=f'Neuron {neuron_index}')

plt.xlabel('Time')
plt.ylabel('Normalized Concentration')
plt.title('Concentration vs. Time for Neurons in the Second Layer')
plt.legend()
plt.show()