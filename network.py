# Network class, create and control the neural network

from layer import Layer 
from load.load_label import LoadLabel
from load.load_image import LoadImage

class Network:
    """
    Constructor method

    Parameters:

    * layers_information: Array to contain the number of neurons by layer. e.g:

        [784, 16, 16, 10]
          +   +   +   +
          |   |   |   +-----> layer(4) with 10 neurons
          |   |   |
          |   |   +---------> layer(3) with 16 neurons
          |   |
          |   +-------------> Layer(2) with 16 neurons
          |
          +-----------------> Layer(1) with 784 neurons (WARNING: Input layer)

    """
    def __init__(self, layers_information):
        self.layers = []
        account_layers = len(layers_information)
        for number_neurons in range(0, account_layers):
            self.layers.append(Layer(layers_information[number_neurons]))

    """
    related_layers

    Public method

    This method related each layer with the previous layer calling the assing_vertex
    method from layer class.

    Parameters: -

    Return: -
    """
    def related_layers(self):
        for pre_layer, layer in enumerate(self.layers[1:]):
            layer.assing_vertex(self.layers[pre_layer])

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
        self.__input_layer().assing_neuron_values(first_image)
        self.related_layers()
        for layer in self.layers[1:]:
            layer.active_neurons()

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
        for layer in self.layers:
            print("+++++++++++++++++++++++++++++++++++++")
            layer.print_values()

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

    """
    ___input_layer

    Private method

    This method returns the first layer in self.layers

    Parameters: -

    Return: self.layers[0]
    """
    def __input_layer(self):
        return self.layers[0]

layers_information = [784, 16, 16, 10]
n = Network(layers_information)
n.start()
n.print_network()
