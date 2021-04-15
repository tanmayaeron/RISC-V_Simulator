class buffer:
    
    def __init__(self):
        dict = {}

    def set(self, register_name, register_value):
        self.dict[register_name] = register_value

    def get(self, register_name):
        if register_name in self.dict.keys():
            return self.dict[register_name]
        return None
    
    def flush(self):
        self.dict.clear()