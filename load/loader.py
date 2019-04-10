#!/usr/bin/env python3

# Loader class load the files

class Loader:
    def __init__(self, file_url):
        self.data = []
        self.header = b""
        self.number_elements = b""
        my_file = open(file_url, "rb")
        try:
            byte = my_file.read(1)
            while byte != None:
                print(byte)
                self.data.append(byte)
                byte = my_file.read(1)
        finally:
            my_file.close()
        # Read first 4 bytes to assing in header
        # Read next 4 bytes to assing in number_elements
        self.header = self.data[:4]
        self.number_elements = self.data[:4]

    def elements(self):
        return int.from_bytes(self.number_elements, "big")

    def read_next(self, number):
        self.header = self.my_file.read(number)

loader = Loader('../data/t10k-images-idx3-ubyte')
print(loader.header)
print(loader.elements())
print(loader.read_next(4))
