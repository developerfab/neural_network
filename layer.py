# Layer class contain the neurons

# python classes
import random

# personal classes
from neuron import Neuron

class Layer:
    def __init__(self, count):
       self.neurons = list()
       self.create_neurons(count) 
       self.pre_layer = None

    """
    create_neurons

    Public method

    Parameters:

    * count: Number of neurons to create

    This method create a number specific of neurons

    Return: -
    """
    def create_neurons(self, count):
        for i in range(1, count+1):
            self.neurons.append(Neuron())

    """
    assing_vertex

    Public method

    Parameters:

    * pre_layer: Layer object, previous layer.

    This method allow
    """
    def assing_vertex(self, pre_layer):
        self.pre_layer = pre_layer

        for my_neuron in self.neurons:
            for neuron in pre_layer.neurons:
                my_neuron.assing_vertex(id(neuron), random.random())

    def return_my_neurons_values(self):
        values = { }
        for neuron in self.neurons:
            values[id(neuron)] = neuron.my_value

        return values

    def active_neurons(self):
        neuron_values = self.pre_layer.return_my_neurons_values()
        for neuron in self.neurons:
            neuron.calcule_weigth(neuron_values)
            neuron.activate()

    def active_layer(self):
        for my_neuron in self.neurons:
            my_neuron.active

    def assing_neuron_values(self, values):
        for index in range(1, len(values)):
            self.neurons[index].assing_value(values[index])

    def print_values(self):
        for neuron in self.neurons:
            neuron.print_my_value()

"""
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
"""
