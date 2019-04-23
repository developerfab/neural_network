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

    """
    return_my_neurons_values

    Public method

    This method take each neuron id and each neuron value, and put these
    in an dictionary like:

    { neuron_id: neuron_value, ... }

    Parameters: -

    Return: A dictionary with each neuron information
    """
    def return_my_neurons_values(self):
        values = { }
        for neuron in self.neurons:
            values[id(neuron)] = neuron.my_value

        return values

    """
    active_neurons

    Public method

    This method call the calcule_weigth and activate functions to each neuron
    of this layer.

    Parameters: -

    Returns: -
    """
    def active_neurons(self):
        neuron_values = self.pre_layer.return_my_neurons_values()
        for neuron in self.neurons:
            neuron.calcule_weigth(neuron_values)
            neuron.activate()

    """
    activa_layer

    Public method

    This method activate each neuron layer

    Parameters: -

    Return: -
    """
    def active_layer(self):
        for my_neuron in self.neurons:
            my_neuron.active

    """
    assing_neuron

    Public method

    This method assing the neuron values send though values parameter.
    This method only must use in the first layer, because this layer doesn't
    calcule its value by himself.

    Parameters: 
    * values: Array that contain the values that should be assing in each neuron

    Return: -
    """
    def assing_neuron_values(self, values):
        for index in range(1, len(values)):
            self.neurons[index].assing_value(values[index])

    """
    print_values

    Public method

    This method call in each neuron the method print_my_value.

    Parameters: -

    Return: -
    """
    def print_values(self):
        for neuron in self.neurons:
            neuron.print_my_value()

