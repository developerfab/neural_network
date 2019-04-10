# Class to read the labels files

class LoadLabel:
    def __init__(self, file_url):
        my_file = open(file_url, "rb")
        self.header = my_file.read(4)
        self.number_of_items = int.from_bytes(my_file.read(4), "big")
        self.labels = []
        try:
            group = my_file.read(1)
            while group != b'':
                print(group)
                self.labels.append(group)
                aux = my_file.read(1)
                if aux != b'':
                    group = ord(aux)
                else:
                    break
        finally:
            my_file.close()

