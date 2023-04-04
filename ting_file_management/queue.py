from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or len(self._data) <= index:
            raise IndexError("Índice Inválido ou Inexistente")
        for enum, value in enumerate(self._data):
            if enum == index:
                return value
