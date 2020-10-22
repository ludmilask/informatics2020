class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        if isinstance(other, Dict) or isinstance(other, dict):
            for pair in other.items():
                self[pair[0]] = self[pair[1]]
        else:
            raise ValueError

    def add(self, other):
        return self + other

    @classmethod
    def from_default(cls, default_dict):
        if isinstance(default_dict, dict):
            return Dict(default_dict)
        else:
            raise ValueError
