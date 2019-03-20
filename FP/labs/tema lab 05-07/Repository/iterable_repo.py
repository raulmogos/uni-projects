


class IterableData():

    def __init__(self):
        self.list = []
        self.index = 0

    def __iter__(self):
        return self

    def __setitem__(self, key, value):
        self.list[key] = value

    def __next__(self):
        if self.index >= len(self.list)-1:
            raise StopIteration
        else:
            self.index+=1
            return self.list[self.index]

    def __delitem__(self, key):
        del self.list[key]

    def __getitem__(self, item):
        return self.list[item]

    def append(self, item):
        self.list.append(item)

    def __len__(self):
        return len(self.list)