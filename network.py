# Network class, create and control the neural network

from layer import Layer 

class Network:
    def __init__(self):
        self.input_layer = Layer(784)
        self.second_layer = Layer(16)
        self.third_layer = Layer(16)
        self.output_layer = Layer(10)

    def related_layers(self):
        self.second_layer.assing_vertex(self.input_layer)
        self.third_layer.assing_vertex(self.second_layer)
        self.output_layer.assing_vertex(self.third_layer)

    def import_data(self):
        pass

    def start(self):
        pass
