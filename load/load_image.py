#!/usr/bin/env python3

class LoadImage:
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
        self.number_of_images = int.from_bytes(my_file.read(4), "big")
        # Read the next 4 bytes and convent in integer
        self.number_rows = int.from_bytes(my_file.read(4), "big")
        # Read the next 4 bytes and convent in integer
        self.number_columns = int.from_bytes(my_file.read(4), "big")
        # Empty array where going to save the images 
        # Each 784 bytes is an image. Is important that 
        # this is in order.
        self.images = []
        dimension = self.number_rows * self.number_columns
        try:
            for i in range(0, self.number_of_images):
                image = list(my_file.read(784))
                self.images.append(image)
        finally:
            my_file.close()
        my_file.close()

"""
l = LoadImage('data/t10k-images-idx3-ubyte')
print(l.header)
print(l.number_of_images)
print(l.number_rows)
print(l.number_columns)
# print(l.images)
for image in l.images:
    print("--------------------")
    for row in range(0, 28):
        print([0 if x<127 else 1 for x in image[:28]])
        del image[:28]
"""
