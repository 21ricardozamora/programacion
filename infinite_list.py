class InfiniteList:
    def __init__(self, *args, fill_value=None):
<<<<<<< HEAD
        self.items = list(args)
=======
        self.args = list(args)
        self.items = args
>>>>>>> cb8c2f5857d6124ded63039d97ad5c1f31d4e960
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, items) -> None:
        if isinstance(index, int):
<<<<<<< HEAD
            if index > len(self.items):
                self.items += [self.fill_value] * abs(index - len(self.items) + 1)
            self.items[index] = items
        print(self.args)

=======
            if index >= len(self.args):
                self.args += [self.fill_value] * (index - len(self.args) + 1)
                self.items[index] = self.args    
>>>>>>> cb8c2f5857d6124ded63039d97ad5c1f31d4e960
    def __str__(self):

        return ",".join(str(_) for _ in self.items)
