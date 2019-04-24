# Network class, create and control the neural network

from layer import Layer 
from load.load_label import LoadLabel
from load.load_image import LoadImage

class Network:
    """
    When the creates a new class, it creates 4 layers:

    * 1 layer: 784 neurons
    * 2 layer: 16 neurons
    * 3 layer: 16 neurons
    * 4 layer: 10 neurons

    The 4 layers is the output layer
    """
    def __init__(self):
        self.input_layer = Layer(784)
        self.second_layer = Layer(16)
        self.third_layer = Layer(16)
        self.output_layer = Layer(10)

    """
    related_layers

    Public method

    This method related each layer with the previous layer calling the assing_vertex
    method from layer class.

    Parameters: -

    Return: -
    """
    def related_layers(self):
        self.second_layer.assing_vertex(self.input_layer)
        self.third_layer.assing_vertex(self.second_layer)
        self.output_layer.assing_vertex(self.third_layer)

    """
    start

    This method assing the values in the first layer and call the active_neurons
    in the nexts layers

    Parameters: -

    Return: -
    """
    def start(self):
        images = self.__load_input_data('data/t10k-images-idx3-ubyte')
        first_image = images[0]
        self.input_layer.assing_neuron_values(first_image)
        self.related_layers()
        self.second_layer.active_neurons()
        self.third_layer.active_neurons()
        self.output_layer.active_neurons()

        """
        When the network is ready uncomment it 

        for image in images:
            print(image)
            self.input_layer.assing_neuron_values(image)
        """

    """
    print_network

    This method print the values of each neuron of each layer.

    Parameters: -

    Return: -
    """
    def print_network(self):
        print("+++++++++++++++++++++++++++++++++++++")
        self.input_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.second_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.third_layer.print_values()
        print("+++++++++++++++++++++++++++++++++++++")
        self.output_layer.print_values()


    # PRIVATE

    """
    __load_input_data

    Private method

    This method load the data images calling LoadImage class.

    Parameters: 
    * url: Route where there are the data

    Return: Array with the data information loaded
    """
    def __load_input_data(self, url):
        return LoadImage(url).images


n = Network()
n.start()
n.print_network()
