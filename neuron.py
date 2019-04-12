# Neuron class

import math
import random

class Neuron:
    def __init__(self):
        self.value = 0
        self.bias = random.random()
        self.vertex_information = { }
        self.my_value = 0

    """
    calcule_wight

    Public method

    It function calcule the sum of the products between the vertex
    and the neural values, and assing that response in self.value

    params:
    * neuron_weights = { object_id: neural value }

    Return: -
    """
    def calcule_weigth(self, neuron_weights):
        total = 0
        for key in neuron_weights:
            total += self.vertex_information[key] * neuron_weights[key]
        self.value = total - self.bias

    """
    activate

    It function evaluate if the value returned by the logistic function
    is greather than zero, if it self.my_value save that value. Otherwise
    self.value contain zero like defeault value.
    """
    def activate(self):
        temporal_value = self.__logistic_function()
        if (temporal_value > 0):
            self.my_value = temporal_value
        else:
            self.my_value = 0


    """
    assing_vertex

    Public method

    It function assing the weight between two neurals(the vertex)
    in the dictionay named: vertex_information. It dictionaty contain
    the next structure:

    vertex_information = { object_id: vertex_weight }

    params:

    * id_neuron: Identifier object of the neural.
    * vertex_weight: Weigth assing to the conection.

    Return: None
    """
    def assing_vertex(self, id_neuron, vertex_weight):
        self.vertex_information[id_neuron] = vertex_weight

    """
    assing_value

    Public method

    Parameters: 
    
    * new_value: Value that going to assing

    This method allow assing directly the value in a neuron, this
    is util then the neuron belongs to the input layer.

    Return: -
    """
    def assing_value(self, new_value):
        self.my_value = new_value

    def print_my_value(self):
        print(self.my_value)

    # PRIVATE METHODS

    """
    __logistic_function

    Private method

    It method return the response of the self.value applyed in the
    logistic function.

    Parameters: None

    Return: self.value apply in the logistic function
    """
    def __logistic_function(self):
        return (1 / (1 + math.exp(-self.value)))

