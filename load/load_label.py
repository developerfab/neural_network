# Class to read the labels files

class LoadLabel:
    """
    Constructor class

    Params:

    * file_url: Url where is located the file
    """
    def __init__(self, file_url):
        # Open de file
        my_file = open(file_url, "rb")
        # Read the firsts 4 bytes(32 bits)
        self.header = my_file.read(4)
        # Read the next 4 bytes and convent in integer
        self.number_of_items = int.from_bytes(my_file.read(4), "big")
        # Empty array where going to save the labels
        # Each byte contain a label. Is important that 
        # this is in order.
        self.labels = []
        try:
            byte_label = my_file.read(1)
            while byte_label != b'':
                self.labels.append(byte_label)
                aux = my_file.read(1)
                if aux != b'':
                    byte_label = ord(aux)
                else:
                    break
        finally:
            my_file.close()

"""
Example to load a file:
l = LoadLabel('data/t10k-labels-idx1-ubyte')
print(l.header)
print(l.number_of_items)
print(l.labels)
"""
