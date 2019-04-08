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
        for i in range(1, count+1):
            self.neurons.append(Neuron())

    def assing_vertex(self, pre_layer):
        for my_neuron in self.neurons:
            for neuron in pre_layer.neurons:
                my_neuron.assing_vertex(id(neuron), random.randint(1,1000))

    def active_layer(self):
        for my_neuron in self.neurons:
            my_neuron.active

layer1 = Layer(3)
print(layer1.neurons)
layer2 = Layer(3)
print(layer2.neurons)

# related layers
print("---- Related Layers ----")
layer2.assing_vertex(layer1)
for neuron in layer2.neurons:
    print neuron
    print neuron.vertex_information
