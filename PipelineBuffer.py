from collections import defaultdict


class Buffer:

    def __init__(self):
        self.dict = defaultdict(int)

    def set(self, register_name, register_value):
        self.dict[register_name] = register_value

    def get(self, register_name):
        if register_name in self.dict:
            return self.dict[register_name]

    def flush(self):
        self.dict.clear()
