# A customize iterator may be used to iterate over the real-time data.


class MyIterator:
    # TODO: implement this class
    def __init__(self):
        self.length = None
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.length

    def reset(self):
        self.index = 0

    def __next__(self):
        if self.index < len(self.length):
            result = self.get(self.index)
            self.index += 1
            return result
        else:
            raise StopIteration

    def get(self, index):
        pass
