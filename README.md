# Spiking Neural Networks with Biologically Inspired Learning

This project delves into the world of spiking neural networks (SNNs) using the computationally efficient **FitzHugh-Nagumo (FHN)** model and the **Spike Timing Dependent Plasticity (STDP)** learning rule. We aim to create an SNN that mimics the biological underpinnings of how neurons learn and process information.

## Core Concepts
- **Spiking Neural Networks**: Inspired by the human brain, SNNs process information through discrete `spikes` fired by the neurons. This project utilizes the FHN model, a simplified yet powerful representation of real neuron dynamics.
- **FitzHugh-Nagumo (FHN) Model**: This model captures the essence of neuron behavior with two variables: `Voltage (V)` and a `Recovery Variable (w)`. It offers a balance between biological plausibility and computational tractability.
- **Spike Timing Dependent Plasticity**: This learning rule strengthens or weakens connections between neurons based on the timing of their spikes. It reflects the biological phenomenon of synaptic plasticity, where experience shapes neural connections.

## Project Goals
- `Implement an SNN`: We construct a network of FHN neurons, mimicking biological neural interactions.
- `Simulate STDP Learning`: The network dynamically adjusts synaptic weights based on spike timing, mimicking how neurons learn.
- `Analyze Learning and Processing`: We evaluate the network's ability to process information and adapt through STDP.
- `Bridge the Biological Gap`: We validate the biophysical interpretation of the Hodgkin-Huxley model (a more complex neuron model) through the FHN model and STDP.
- `Unify Mathematical and Biological Models`: We aim to create a comprehensive understanding of learning in SNNs by connecting mathematical models with their biological counterparts.

## Getting Started
This project requires Python, and NumPy. You can optionally use libraries like Matplotlib for visualization.

1. Clone the repository
```r
git clone https://github.com/anshul-2010/Transport-Phenomenon-in-Biological-Systems.git
```

2. Install the dependencies
```r
pip install numpy
pip install matplotlib
```

3. Run the scripts
```r
python Hierarchical_Connectivity.py
python Mass_Flux_Matrix.py
python Concentration_Profile.py
python Modeling_SNN_STDP.py
```
The script defines the network architecture, learning parameters, simulation conditions, and performs the analysis.

## Further directions
* `Enhanced Biorealism`: We plan to incorporate more complex neuron models while retaining STDP, potentially revealing new learning mechanisms.
* `Multi-Sensory Integration`: The project can be extended to explore how SNNs process information from various sensory modalities, paving the way for advanced neuromorphic systems.
* `Neuromorphic Hardware`: Insights from this project can be translated into energy-efficient neuromorphic hardware, potentially revolutionizing AI and cognitive neuroscience.
