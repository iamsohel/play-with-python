from abc import ABC, abstractclassmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed")
        self.opened = False

    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading from file stream")


class NetworkStream(Stream):
    def read(self):
        print("reading from network stream")


class MemoryStream(Stream):
    def read(self):
        print("reading from memory")


file = FileStream()
file.read()

memory = MemoryStream()
