# Neuron class

import math

class Neuron:
    """
    neuron_weights = { object_id: individual weight }
    bias = Activate value
    """
    def __init__(self, neuron_weights, bias):
        self.weight = 0
        self.bias = bias
        self.calcule_weigth(neuron_weights)
        self.vertex_information = { }
        self.my_value = 0

    def calcule_weigth(self, neuron_weights):
        total = 0
        for key in neuron_weights:
            total += self.vertex_information[key] * neuron_weights[key]
        self.weight = total - self.bias

    def activate(self):
        temporal_value = self.logistic_function()
        if (temporal_value > 0):
            self.my_value = temporal_value

    def neurons(self, id_neuron, vertex_weight):
        self.vertex_information[id_neuron] = vertex_weight

    def logistic_function(self):
        return (1 / (1 + math.exp(-self.weight)))

