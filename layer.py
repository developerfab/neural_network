# Layer class contain the neurons

# python classes
import random

# personal classes
from neuron import Neuron

class Layer:
    def __init__(self, count):
       self.neurons = list()
       self.create_neurons(count) 

    def create_neurons(self, count):
        for i in range(1, count):
            self.neurons.append(Neuron(random.random(), 0))

layer = Layer(3)
layer.neurons
