from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text file..."

    def write(self, data):
        print(f"Writing '{data}' to text file.")

class BinaryFileHandler(FileHandler):
    def read(self):
        return b"Binary data"

    def write(self, data):
        print(f"Writing binary data: {data}")

text_handler = TextFileHandler()
print(text_handler.read())
text_handler.write("Hello")

binary_handler = BinaryFileHandler()
print(binary_handler.read())
binary_handler.write(b"101010")
