# Network class, create and control the neural network

from layer import Layer 
from load.load_label import LoadLabel
from load.load_image import LoadImage

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

    def start(self):
        images = self.__load_input_data('data/t10k-images-idx3-ubyte')
        first_image = images[0]
        self.input_layer.assing_neuron_values(first_image)
        self.related_layers()
        self.second_layer.active_neurons()
        self.third_layer.active_neurons()
        self.output_layer.active_neurons()
        print("+++++++++++++++++++++++++++++++++++++")
        self.input_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.second_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.third_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.output_layer.print_values()

        """
        When the network is ready uncomment it 

        for image in images:
            print(image)
            self.input_layer.assing_neuron_values(image)
        """

    # PRIVATE

    def __load_input_data(self, url):
        return LoadImage(url).images


n = Network()
n.start()
