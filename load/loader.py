#!/usr/bin/env python3

# Loader class load the files

class Loader:
    def __init__(self, file_url):
        self.header = b""
        self.number_elements = b""
        self.my_file = open(file_url, "rb")
        # Read first 4 bytes to assing in header
        # Read next 4 bytes to assing in number_elements
        self.header = self.my_file.read(4)
        self.number_elements = self.my_file.read(4)

    def elements(self):
        return int.from_bytes(self.number_elements, "big")

    def read_next(self, number):
        pass

l = Loader('../data/t10k-images-idx3-ubyte')
print(l.elements)
